# Generated by Django 3.2.12 on 2022-03-02 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('Date_of_birth', models.DateField()),
                ('PhoneNumber', models.CharField(max_length=500)),
                ('Address_Employee', models.CharField(max_length=1000)),
                ('Department', models.CharField(max_length=500)),
                ('Position_Employee', models.CharField(max_length=500)),
            ],
        ),
    ]