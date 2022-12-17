from django.db import models

class patient(models.Model):
    name=models.CharField(max_length=50,default="")
    phone_no=models.IntegerField(max_length=10,default="")
    address=models.CharField(max_length=200,default="")
    def __str__(self):
         return self.name
class Doctor(models.Model):
    name=models.CharField(max_length=50,default="")
    department=models.CharField(max_length=100,default="")
    category=models.CharField(max_length=50,default="")
    def __str__(self):
         return self.name
class Nurse(models.Model):
    name=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class Prescription(models.Model):
    prescription=models.CharField(max_length=500,default="")
    doctor_id=models.ForeignKey(Doctor, related_name = "doctor",on_delete=models.PROTECT)

class PatientFeedback(models.Model):
    patient_id=models.ForeignKey(patient, related_name = "patient",on_delete=models.PROTECT)
    feedback=models.CharField(max_length=500,default="")
def __str__(self):
        return self.feedback
class discussion(models.Model):
    discussion=models.CharField(max_length=500,default="")
def __str__(self):
        return self.discussion