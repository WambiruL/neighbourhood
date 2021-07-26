import neighbourhood
from django.shortcuts import render,redirect
from .forms import CreateUserForm,UserUpdateForm,ProfleUpdateForm
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

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

def lanetBusiness(request):
   lanet_neighbourhood = Neighbourhood.objects.get(pk=1)
   businesses = Business.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'Lanetbusiness.html', {'businesses':businesses})

def milimaniBusiness(request):
   milimani_neighbourhood = Neighbourhood.objects.get(pk=3)
   businesses = Business.objects.filter(neighbourhood=milimani_neighbourhood)
   return render(request,'Milimanibusiness.html', {'businesses':businesses})

def kiamunyiBusiness(request):
   kiamunyi_neighbourhood = Neighbourhood.objects.get(pk=2)
   businesses =  Business.objects.filter(neighbourhood=kiamunyi_neighbourhood)
   return render(request,'business.html', {'businesses':businesses})


def lanetAuth(request):
   lanet_neighbourhood = Neighbourhood.objects.get(pk=1)
   authorities = Authorities.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'authorities.html', {'authorities':authorities})

def lanetHealth(request):
   lanet_neighbourhood = Neighbourhood.objects.get(pk=1)
   hcenters = Health.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'health.html', {'hcenters':hcenters})


@login_required(login_url='/login')
def lanet(request):
   lanet= Neighbourhood.objects.get(pk=1)
   return render(request,'lanet.html', {'lanet':lanet})



@login_required(login_url='/login')
def milimani(request):
   milimani= Neighbourhood.objects.get(pk=2)
   return render(request,'milimani.html', {'milimani':milimani})

def kiamunyiBusiness(request):
   kiamunyi_neighbourhood = Neighbourhood.objects.get(pk=3)
   businesses =  Business.objects.filter(neighbourhood=kiamunyi_neighbourhood)
   return render(request,'kiamunyi.html', {'businesses':businesses})


@login_required(login_url='/login')
def kiamunyi(request):
   kiamunyi= Neighbourhood.objects.get(pk=3)
   return render(request,'kiamunyi.html', {'kiamunyi':kiamunyi})

def submitBusiness(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('')
    else:
        form =BusinessUploadForm()
            
    return render(request,'business_form.html',{"form":form,})




