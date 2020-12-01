from django.db import models


class Doctor(models.Model):
    doctor_login = models.CharField(max_length=100)
    doctor_pass = models.CharField(max_length=100)


class Login(models.Model):
    login = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    spec = models.CharField(max_length=50)

class Heal(models.Model):
	problem = models.CharField(max_length=100)
	wiki = models.TextField()