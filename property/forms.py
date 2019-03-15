from django.forms import ModelForm
from .models import PropertyDetails

class PropertySellForm(ModelForm):
    class Meta:
        model = PropertyDetails
        exclude = ["property_doc","property_img"]


