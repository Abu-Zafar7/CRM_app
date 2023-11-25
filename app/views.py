from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import StudentRecord, Detail
from django.utils import timezone
from .forms import StudentsForm, DetailForm


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f'Welcome {user}')
            return redirect('records')
        else:
            messages.error(request, 'You need to login first..')
            return redirect('home')
    else:    
        return render(request,'app/home.html',{})


def student_records(request):
    records = StudentRecord.objects.order_by('sr_no')
    return render(request,'app/records.html',{'records':records})


def add_record(request):
    
    form = StudentsForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if 'save_and_add_another' in request.POST:
                return redirect('add_record')
            else:
                return redirect('records')
    else:
        return render(request, 'app/add_record.html', {'form': form})
   
def edit_record(request,pk):
        current_record = StudentRecord.objects.get(id=pk)
        form = StudentsForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            return redirect('records')
        return render(request, 'app/edit_record.html', {'form': form, 'record': current_record})

def details(request, pk):
    try:
        student = StudentRecord.objects.get(id= pk)
        details = Detail.objects.filter(student = student)
    except Detail.DoesNotExist:
        
        details = Detail()
    
  

    return render(request, 'app/details.html', {'student':student,'details': details})



def add_details(request, pk):
    
    student_record = StudentRecord.objects.get(id=pk)
    form = DetailForm(request.POST or None)
    pk = student_record.id
    if request.method == 'POST':
        if form.is_valid():
            detail = form.save(commit=False)
            detail.student = student_record  
            detail.save()  
            return redirect('details', pk=student_record.id)  
    else:
        return render(request, 'app/add_details.html', {'form': form,'pk': pk}) 
    return render(request, 'app/add_details.html', {'form': form,'pk': pk}) 



def check_due_payments(request):
    
     
    today = timezone.now().date()
    due_student_details = Detail.objects.filter(due_date=today, fee_received=False)

    for detail in due_student_details:
        messages.info(request, f"Payment for {detail.student.name} is due.")

   
    due_tutor_details = Detail.objects.filter(due_date=today, tutor_paid=False)

    for detail in due_tutor_details:
        messages.info(request, f"Tutor payment for {detail.student.name} is due.")      


def delete_record(request,pk):
    record = StudentRecord.objects.get(id=pk)
    record.delete()
    messages.success(request,"Record deleted successfully")
    return redirect("records")

def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out successfully!')
    return redirect('home')