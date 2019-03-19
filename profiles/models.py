from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Userprofiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.IntegerField()
    address = models.CharField(max_length=120)
    pan = models.CharField(max_length= 10)

    def __str__(self):
        return self.user.username