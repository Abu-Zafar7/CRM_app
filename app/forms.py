from django import forms
from .models import StudentRecord, Detail


class StudentsForm(forms.ModelForm):


    sr_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Enter Name", "class":"form-control"}), label="")

    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")

    class_or_school = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Class/School", "class":"form-control"}), label="")

    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    
    tutor_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tutor's Name", "class":"form-control"}), label="")
    subjects = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Subjects", "class":"form-control"}), label="")

    starting_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Starting Date", "class":"form-control", "type": "date"}), label="Starting Date")

    completion_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Completion Date", "class":"form-control","type": "date"}), label="Due Date")

    fee = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Fee", "class":"form-control"}), label="")

    duration = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Duration", "class":"form-control"}), label="")
    

    class Meta:
        model = StudentRecord
        fields = '__all__'


class DetailForm(forms.ModelForm):
    start_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Starting Date", "class":"form-control", "type": "date"}), label="Starting Date")
    due_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Completion Date", "class":"form-control","type": "date"}), label="Due Date")
    class Meta:
        model= Detail
        exclude = ['student']