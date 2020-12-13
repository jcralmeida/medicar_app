from django.contrib import admin

from medicar_api.models import Schedule
from django.forms import ValidationError, ModelForm


class ScheduleForm(ModelForm):
    """
    Represent the class for validate the values of the Schedule model.
    """
    class Meta:
        model = Schedule
        fields = '__all__'

    def clean(self):
        """
        Validate if the client is trying to register a schedule to a doctor who
        already has a schedule for a specific day.
        """

        doctor = self.cleaned_data.get("medico")
        day = self.cleaned_data.get('dia')

        retrieved_schedule = Schedule.objects.filter(medico=doctor, dia=day).all()

        if retrieved_schedule:
            raise ValidationError("There is already a schedule for this doctor.")

        return self.cleaned_data


class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleForm
    list_display = ('medico', 'dia', 'horario')