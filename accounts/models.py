from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100, default='')
    grand_father_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=15, default='')
    age = models.IntegerField(default='')
    gender = models.CharField(max_length=100, default='0')
    provience_number = models.CharField(max_length=15, default='0')
    district = models.CharField(max_length=15, default='0')
    token = models.CharField(max_length=100, default='')


    def __str__(self):
        return str(self.father_name)