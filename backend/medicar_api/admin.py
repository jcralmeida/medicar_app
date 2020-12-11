from django.contrib import admin

# Register your models here.
from medicar_api.models import Specialty, Doctor, Schedule

admin.site.register(Specialty)
admin.site.register(Doctor)
admin.site.register(Schedule)