from django.shortcuts import render
from django.http import HttpResponse

from .models import PropertyDetails

from .forms  import PropertySellForm

# Create your views here.
def home_view(request):
    template_name = "property/home.html"
    context_data = {}

    return render(request,template_name,context_data)

def contact_view(request):
    template_name = "property/contact.html"
    context_data = {}

    return render(request,template_name,context_data)


def about_view(request):
    template_name = "property/about.html"
    context_data = {}

    return render(request,template_name,context_data)

def property_list(request):
    template_name = "property/buy.html"
    property_data = PropertyDetails.objects.all()
    print("Queryset DATA is:   ",property_data)
    context_data = {
        'data':property_data
    }
    return render(request,template_name,context_data)


def property_sell(request):
    template_name = "property/sell.html"
    form = PropertySellForm(request.POST)
    if form.is_valid():
        form.save()
    context_data = {
        'form':PropertySellForm
    }

    return render(request,template_name,context_data)