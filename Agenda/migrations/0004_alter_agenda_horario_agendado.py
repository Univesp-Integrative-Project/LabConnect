# Generated by Django 5.0.3 on 2024-04-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0003_alter_agenda_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='horario_agendado',
            field=models.CharField(choices=[('1', '08:00h às 09:00h'), ('2', '09:00h às 10:00h'), ('3', '10:00h às 11:00h'), ('4', '11:00h às 12:00h')], max_length=20),
        ),
    ]