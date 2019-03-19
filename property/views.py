from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import PropertyDetails
from django.views  import View
from .forms  import PropertySellForm
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def home_view(request):
    template_name = "property/home.html"
    context_data = {}

    return render(request,template_name,context_data)

@login_required
def contact_view(request):
    template_name = "property/contact.html"
    context_data = {}

    return render(request,template_name,context_data)

@login_required
def about_view(request):
    template_name = "property/about.html"
    context_data = {}

    return render(request,template_name,context_data)

class AboutView(LoginRequiredMixin,View):
    login_url = '/login/'
    template_name = "property/about.html"
    context_data = {}

    def get(self, request):
        return render(request,self.template_name,self.context_data)

@login_required
def property_list(request):
    template_name = "property/buy.html"
    property_data = PropertyDetails.objects.all()
    print("Queryset DATA is:   ",property_data)
    context_data = {
        'data':property_data
    }
    return render(request,template_name,context_data)


class PropertyList(LoginRequiredMixin,ListView):
    login_url = "/login/"
    model = PropertyDetails
    template_name = "property/buy.html"

class PropertyDetail(LoginRequiredMixin,DetailView):
    login_url = "/login/"
    model = PropertyDetails
    template_name = "property/detail.html"

class PropertyDelete(LoginRequiredMixin,DeleteView):
    login_url = "/login/"
    model = PropertyDetails
    template_name = "property/delete.html"
    success_url = reverse_lazy('property:buy')



class PropertyUpdate(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    model = PropertyDetails
    fields = "__all__"
    template_name = "property/update.html"
    success_url = reverse_lazy('property:buy')


class PropertyCreate(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    model = PropertyDetails
    fields = ["property_name",
              "property_address",
              "property_age",
              "property_price",
              "property_doc",
              "property_img",
              "property_facing"]

    template_name = "property/sell.html"
    success_url = reverse_lazy('property:buy')

    def form_valid(self,form):
        form.instance.user_data = self.request.user
        return super().form_valid(form)

@login_required
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