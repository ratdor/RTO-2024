# Generated by Django 5.0.4 on 2024-06-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rtoapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gpsvehicle",
            name="chassis_no",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="dealer",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="engine_no",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="gps_model",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="gps_serial_no",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="location_primary",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="mobile_no",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="network",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="registration_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="registration_no",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="vehicle_make",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="gpsvehicle",
            name="vehicle_model",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
