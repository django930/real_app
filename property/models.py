from django.db import models

# Create your models here.
class PropertyDetails(models.Model):

    Facing_choices = (
        ("N","North"),
        ("W","West"),
        ("E","East"),
        ("S","South")
    )

    property_name = models.CharField(max_length=25,unique=True)
    property_address = models.CharField(max_length=255)
    property_age = models.IntegerField()
    property_price = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    property_doc = models.FileField(blank=True, null=True)
    property_img = models.ImageField(blank=True, null=True)
    property_facing = models.CharField(max_length=1,choices=Facing_choices,default="N")


    def __str__(self):
        return self.property_name