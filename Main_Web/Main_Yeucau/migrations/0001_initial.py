# Generated by Django 3.2.12 on 2022-03-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='yeucaudaduyet',
            fields=[
                ('YeucauId', models.AutoField(primary_key=True, serialize=False)),
                ('NguoiyeucauId', models.CharField(max_length=10)),
                ('Nguoiyeucau', models.CharField(max_length=500)),
                ('Thongtinyeucau', models.CharField(max_length=500)),
                ('Lydo', models.CharField(max_length=5000)),
                ('Nguoiduyet', models.CharField(max_length=1000)),
                ('Ngaygui', models.DateField(auto_now_add=True)),
                ('thoigianbatdau', models.DateTimeField()),
                ('thoigianketthuc', models.DateTimeField()),
                ('Trangthaiduyet', models.CharField(max_length=10)),
            ],
        ),
    ]
