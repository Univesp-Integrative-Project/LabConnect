from django import forms
from django.forms.widgets import DateInput
from .models import Agenda

class AgendaModelForm(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = ['escola', 'laboratorio',
                  'disciplina', 'turma', 'data_agendada', 'horario_agendado']
        widgets = {
            'data_agendada': DateInput(attrs={'type': 'date'})
        }
