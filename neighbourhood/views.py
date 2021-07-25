import neighbourhood
from django.shortcuts import render,redirect
from .forms import CreateUserForm,UserUpdateForm,ProfleUpdateForm
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context={'form':form}
    return render(request,'registration/registration.html',context)

@login_required(login_url='/login')
def index(request):
    neighbourhood=Neighbourhood.objects.all()

    context={
        "neighbourhood":neighbourhood,
    }
    return render(request,'index.html',context)

def profileView(request):
    logged_in_user=request.user #logged in user
    user=Profile.objects.get(user=logged_in_user)
    print(user)
    
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfleUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfleUpdateForm(instance=request.user.profile)
    ctx={
        "user":user,
        'u_form':u_form,
        'p_form':p_form
    }
   
    return render(request,'profile.html',ctx)

def lanet(request):
   lanet_neighbourhood = Neighbourhood.objects.get(pk=1)
   lanet = Neighbourhood.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'lanet.html', {'lanet':lanet})

def milimani(request):
   milimani_neighbourhood = Neighbourhood.objects.get(pk=2)
   milimani = Neighbourhood.objects.filter(neighbourhood=milimani_neighbourhood)
   return render(request,'milimani.html', {'milimani':milimani})




