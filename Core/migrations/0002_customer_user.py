# Generated by Django 4.1.6 on 2023-02-21 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.user'),
        ),
    ]