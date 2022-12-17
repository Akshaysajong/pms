from django.contrib import admin

from .models import*
admin.site.register(patient)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(PatientFeedback)
# Register your models here.
