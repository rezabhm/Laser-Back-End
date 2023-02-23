# Generated by Django 4.1.6 on 2023-02-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_forgotpassword_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='charge',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forgotpassword',
            name='code',
            field=models.CharField(default='****', max_length=8, primary_key=True, serialize=False),
        ),
    ]