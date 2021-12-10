from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    phone_num = models.CharField(max_length=15, default='0')
    age = models.IntegerField(default='0')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, default='0')


    def __str__(self):
        return str(self.user)