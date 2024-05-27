# Generated by Django 5.0.3 on 2024-05-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0004_alter_agenda_horario_agendado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='horario_agendado',
            field=models.CharField(choices=[('1', '07:30h às 08:20h'), ('2', '08:20h às 09:10h'), ('3', '09:10h às 10:00h'), ('4', '10:20h às 11:10h'), ('5', '11:10h às 12:00h'), ('6', '12:10h às 12:50h'), ('7', '13:00h às 13:50h'), ('8', '13:50h às 14:40h'), ('9', '14:40h às 15:30h'), ('10', '15:30h às 15:50h'), ('11', '15:50h às 16:40h'), ('12', '16:40h às 17:30h'), ('13', '17:30h às 18:20h'), ('14', '19:20h às 20:05h'), ('15', '21:10h às 21:55h')], max_length=20),
        ),
    ]