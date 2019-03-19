from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import Userprofiles
from django.db import IntegrityError
from django.urls import reverse_lazy
from property.models import PropertyDetails

# Create your views here.
def LoginView(request):
    template_name="profiles/login.html"
    error_message = ""

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("user is: ",user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
            error_message = "Username or password is incorrect."

    context = {
        'error':error_message
    }
    return render(request,template_name,context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def registration(request):
    template_name = "profiles/reg.html"
    error_message = ""
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return HttpResponseRedirect(reverse('login'))
    else:
            error_message = "Username or password is incorrect."

    context = {

    }
    return render(request,template_name,context)



def profile_view(request):
    template_name = "profiles/profile.html"
    profile = Userprofiles.objects.get(user=request.user)
    properties = PropertyDetails.objects.filter(user_data = request.user)

    context = {
            'profile':profile,
            'properties':properties
    }


    return render(request,template_name,context)


def profile_update_view(request):
        if request.POST:
                mobile = request.POST.get('mobile')
                address = request.POST.get('address')
                pan = request.POST.get('pan')
                user = request.user
                try:
                        new_object = Userprofiles.objects.update_or_create(user=user,
                                                    address=address,
                                                    mobile=mobile,
                                                    pan=pan)
                except IntegrityError:
                        obj = UserProfiles.objects.get(user=request.user)
                        obj.address = address
                        obj.mobile = mobile
                        obj.pan = pan
                        obj.save()
                return HttpResponseRedirect(reverse_lazy('profile'))
        template_name = "profiles/updateprofile.html"
        context = {

        }
        return render(request,template_name,context)