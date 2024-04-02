from django.db import models
from django.contrib.auth.models import User

class Escola(models.Model):
    """Classe representando uma escola"""
    id_escola = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Turma(models.Model):
    """Classe representando a turma de uma escola"""
    id_turma = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

class Laboratorio(models.Model):
    """Classe representando um laboratório da escola"""
    id_laboratorio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

class Disciplina(models.Model):
    """Classe representando uma disciplina da escola"""
    id_disciplina = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Agenda(models.Model):
    """Clsse representando um agendamento realizado"""
    HORARIO_CHOICES=[('1','08:00h às 09:00h'),
                     ('2','09:00h às 10:00h'),
                     ('3','10:00h às 11:00h'),
                     ('4','11:00h às 12:00h'),]
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_agendada = models.DateField()
    horario_agendado = models.CharField(max_length=20, choices=HORARIO_CHOICES)
    data_agendamento = models.DateTimeField(auto_now_add=True)# Data e hora automáticas do agendamento

    def __str__(self):
        return f"Agendamento para {self.disciplina} na data {self.data_agendada} às {self.horario_agendado}"
    
    class Meta:
        # Definindo que a combinação de laboratório, data_agendada e horario_agendado deva ser única
        unique_together = ('laboratorio', 'data_agendada', 'horario_agendado')
