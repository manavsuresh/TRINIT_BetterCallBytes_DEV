# Generated by Django 4.1 on 2024-03-10 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LinguaConnect', '0003_alter_teacher_profeciency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Profeciency',
            new_name='Proficiency',
        ),
    ]