from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import PropertyDetails
from django.views  import View
from .forms  import PropertySellForm
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView

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

class AboutView(View):
    template_name = "property/about.html"
    context_data = {}

    def get(self, request):
        return render(request,self.template_name,self.context_data)

def property_list(request):
    template_name = "property/buy.html"
    property_data = PropertyDetails.objects.all()
    print("Queryset DATA is:   ",property_data)
    context_data = {
        'data':property_data
    }
    return render(request,template_name,context_data)


class PropertyList(ListView):
    model = PropertyDetails
    template_name = "property/buy.html"

class PropertyDetail(DetailView):
    model = PropertyDetails
    template_name = "property/detail.html"

class PropertyDelete(DeleteView):
    model = PropertyDetails
    template_name = "property/delete.html"
    success_url = reverse_lazy('property:buy')



class PropertyUpdate(UpdateView):
    model = PropertyDetails
    fields = "__all__"
    template_name = "property/update.html"
    success_url = reverse_lazy('property:buy')


class PropertyCreate(CreateView):
    model = PropertyDetails
    fields = ["property_name","property_address","property_age","property_price","property_facing"]
    template_name = "property/sell.html"
    success_url = reverse_lazy('property:buy')

def property_sell(request):
    template_name = "property/sell.html"
    form = PropertySellForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('property:buy'))

    context_data = {
        'form':PropertySellForm
    }

    return render(request,template_name,context_data)