from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_property_images(instance,filename):
    return "images/%s/%s" %(instance.id,filename)

def upload_property_doc(instance,filename):
    return "document/%s/%s" %(instance.id,filename)

class PropertyDetails(models.Model):

    Facing_choices = (
        ("N","North"),
        ("W","West"),
        ("E","East"),
        ("S","South")
    )
    user_data = models.ForeignKey(User,on_delete=models.CASCADE)
    property_name = models.CharField(max_length=25,unique=True)
    property_address = models.CharField(max_length=255)
    property_age = models.IntegerField()
    property_price = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    property_doc = models.FileField(upload_to='document/')
    property_img = models.ImageField(upload_to=upload_property_images)
    property_facing = models.CharField(max_length=1,choices=Facing_choices,default="N")


    def __str__(self):
        return self.property_name