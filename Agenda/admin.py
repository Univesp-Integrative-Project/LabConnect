from django.contrib import admin

from .models import Agenda, Disciplina, Escola, Laboratorio, Turma

@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'escola')

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'escola')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('escola', 'usuario', 'laboratorio', 'disciplina', 'turma', 'data_agendada',
                    'horario_agendado' ,'data_agendamento')
