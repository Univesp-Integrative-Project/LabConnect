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
    HORARIO_CHOICES=[('1','07:30h às 08:20h'),
                     ('2','08:20h às 09:10h'),
                     ('3','09:10h às 10:00h'),
                     ('4','10:20h às 11:10h'),
                     ('5','11:10h às 12:00h'),
                     ('6','12:10h às 12:50h'),
                     ('7','13:00h às 13:50h'),
                     ('8','13:50h às 14:40h'),
                     ('9','14:40h às 15:30h'),
                     ('10','15:30h às 15:50h'),
                     ('11','15:50h às 16:40h'),
                     ('12','16:40h às 17:30h'),
                     ('13','17:30h às 18:20h'),
                     ('14','19:20h às 20:05h'),
                     ('15','21:10h às 21:55h'),]
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
