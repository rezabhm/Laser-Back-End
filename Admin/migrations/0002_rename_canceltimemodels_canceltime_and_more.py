# Generated by Django 4.1.6 on 2023-02-06 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CancelTimeModels',
            new_name='CancelTime',
        ),
        migrations.RenameModel(
            old_name='OperatorProgramModels',
            new_name='OperatorProgram',
        ),
    ]
