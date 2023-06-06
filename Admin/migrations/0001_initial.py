# Generated by Django 4.1.6 on 2023-05-19 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelTime',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('start_time_int', models.FloatField(default=0.0)),
                ('start_time_str', models.CharField(max_length=50)),
                ('end_time_int', models.FloatField(default=0.0)),
                ('end_time_str', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OperatorProgram',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('operator_name', models.CharField(default='UnKnow', max_length=20, null=True)),
                ('date_int', models.FloatField(default=0.0)),
                ('date_str', models.CharField(default='-', max_length=50)),
                ('program_turn', models.CharField(choices=[('m', 'morning'), ('a', 'afternoon')], default='m', max_length=1)),
                ('operator', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='Core.user')),
            ],
        ),
    ]
