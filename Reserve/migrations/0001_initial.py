# Generated by Django 4.1.6 on 2023-02-15 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Core', '0001_initial'),
        ('LazerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('session_number', models.IntegerField()),
                ('reserve_type', models.CharField(choices=[('co', 'complete'), ('do', 'done'), ('ca', 'cancel'), ('pe', 'pending'), ('wa', 'waiting'), ('sc', 'system cancel')], max_length=2)),
                ('online_reserve', models.BooleanField(default=True)),
                ('charge', models.BooleanField(default=False)),
                ('payed', models.BooleanField(default=False)),
                ('total_price_amount', models.FloatField()),
                ('total_payment_amount', models.FloatField()),
                ('reserve_time_int', models.FloatField(default=0.0)),
                ('reserve_time_str', models.CharField(default='-', max_length=25)),
                ('request_time_int', models.FloatField(default=0.0)),
                ('request_time_str', models.CharField(default='-', max_length=25)),
                ('laser_area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LazerApp.laserareainformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Core.user')),
            ],
        ),
        migrations.CreateModel(
            name='PreReserve',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('reserve_num', models.IntegerField()),
                ('last_date', models.CharField(max_length=50)),
                ('laser_area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LazerApp.laserareainformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Core.user')),
            ],
        ),
    ]
