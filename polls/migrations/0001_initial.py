# Generated by Django 3.1.3 on 2020-11-30 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_login', models.CharField(max_length=100)),
                ('doctor_pass', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('spec', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.doctor')),
            ],
        ),
    ]
