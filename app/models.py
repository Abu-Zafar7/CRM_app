
from django.db import models


class StudentRecord(models.Model):
    sr_no = models.CharField(max_length=10000,null=True, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null= True)
    class_or_school = models.CharField(max_length=100)
    address = models.TextField()
    tutor_name = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    starting_date = models.DateField()
    completion_date = models.DateField(null=True)
    fee = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
   

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         max_serial_number = StudentRecord.objects.aggregate(models.Max('sr_no'))['sr_no__max']
    #         if max_serial_number is None:
    #             max_serial_number = 0
    #         self.sr_no = max_serial_number + 1

    #     super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name  
    


class Detail(models.Model):
    student = models.ForeignKey(StudentRecord, on_delete=models.CASCADE) 
    start_date = models.DateField(blank=True)
    due_date = models.DateField(blank=True)
    fee_received = models.BooleanField(default=False)
    fee = models.CharField(max_length=100,blank=True)
    received_date = models.DateField(blank=True)
    mode_of_payment = models.CharField(max_length=100, blank=True)
    receipt = models.CharField(max_length=100,blank=True)
    tutor_paid = models.BooleanField(default=False)
    tutor_fee = models.CharField(max_length=100,blank= True)
    date_of_payment = models.DateField(blank=True)
    
    # def __str__(self) -> str:
    #     return self.student
    

