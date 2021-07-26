import neighbourhood
from django.shortcuts import render,redirect
from .forms import CreateUserForm,UserUpdateForm,ProfleUpdateForm
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import get_object_or_404


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
   lanet_neighbourhood = Neighbourhood.objects.filter(pk=1)
   businesses = Business.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'Lanetbusiness.html', {'businesses':businesses})

def milimaniBusiness(request):
   milimani_neighbourhood = Neighbourhood.objects.filter(pk=3)
   businesses = Business.objects.filter(neighbourhood=milimani_neighbourhood)
   return render(request,'Milimanibusiness.html', {'businesses':businesses})

def kiamunyiBusiness(request):
   kiamunyi_neighbourhood = Neighbourhood.objects.filter(pk=2)
   businesses =  Business.objects.filter(neighbourhood=kiamunyi_neighbourhood)
   return render(request,'Kiamunyibusiness.html', {'businesses':businesses})


def lanetAuth(request):
   lanet_neighbourhood = Neighbourhood.objects.filter(pk=1)
   authorities = Authorities.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'Lanetauthorities.html', {'authorities':authorities})

def kiamunyiAuth(request):
   kiamunyi_neighbourhood =Neighbourhood.objects.filter(pk=2)
   authorities = Authorities.objects.filter(neighbourhood=kiamunyi_neighbourhood)
   return render(request,'Kiamunyiauthorities.html', {'authorities':authorities})

def milimaniAuth(request):
   milimani_neighbourhood = Neighbourhood.objects.filter(pk=3)
   authorities = Authorities.objects.filter(neighbourhood=milimani_neighbourhood)
   return render(request,'Milimaniauthorities.html', {'authorities':authorities})

def lanetHealth(request):
   lanet_neighbourhood = Neighbourhood.objects.filter(pk=1)
   hcenters = Health.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'Lanethealth.html', {'hcenters':hcenters})

def milimaniHealth(request):
   milimani_neighbourhood = Neighbourhood.objects.filter(pk=3)
   hcenters = Health.objects.filter(neighbourhood=milimani_neighbourhood)
   return render(request,'Milimanihealth.html', {'hcenters':hcenters})

def kiamunyiHealth(request):
   kiamunyi_neighbourhood = Neighbourhood.objects.filter(pk=2)
   hcenters = Health.objects.filter(neighbourhood=kiamunyi_neighbourhood)
   return render(request,'Kiamunyihealth.html', {'hcenters':hcenters})

def lanetPost(request):
   lanet_neighbourhood= Neighbourhood.objects.filter(pk=1)
   posts = BlogPost.objects.filter(neighbourhood=lanet_neighbourhood)
   return render(request,'LanetPosts.html', {'posts':posts})

def milimaniPost(request):
   milimani_neighbourhood = Neighbourhood.objects.filter(pk=3)
   posts = BlogPost.objects.filter(neighbourhood=milimani_neighbourhood)
   return render(request,'MilimaniPosts.html', {'posts':posts})

def kiamunyiPost(request):
   kiamunyi_neighbourhood = Neighbourhood.objects.filter(pk=2)
   posts = BlogPost.objects.filter(neighbourhood=kiamunyi_neighbourhood)
   return render(request,'KiamunyiPosts.html', {'posts':posts})


@login_required(login_url='/login')
def lanet(request):
   lanet= Neighbourhood.objects.filter(pk=1)
   return render(request,'lanet.html', {'lanet':lanet})


@login_required(login_url='/login')
def milimani(request):
   milimani= Neighbourhood.objects.filter(pk=3)
   return render(request,'milimani.html', {'milimani':milimani})

@login_required(login_url='/login')
def kiamunyi(request):
   kiamunyi= Neighbourhood.objects.filter(pk=2)
   return render(request,'kiamunyi.html', {'kiamunyi':kiamunyi})


def submitBusinessK(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('Kbusiness')
    else:
        form =BusinessUploadForm()
            
    return render(request,'business_form.html',{"form":form,})

def submitBusinessL(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('Lbusiness')
    else:
        form =BusinessUploadForm()
            
    return render(request,'business_form.html',{"form":form,})

def submitBusinessM(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('Mbusiness')
    else:
        form =BusinessUploadForm()
            
    return render(request,'business_form.html',{"form":form,})

def submitPostL(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('LPosts')
    else:
        form =PostUploadForm()
            
    return render(request,'post_form.html',{"form":form,})

def submitPostK(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('KPosts')
    else:
        form =PostUploadForm()
            
    return render(request,'post_form.html',{"form":form,})

def submitPostM(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('MPosts')
    else:
        form =PostUploadForm()
            
    return render(request,'post_form.html',{"form":form,})

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_businesses})

    else:
        message="You can have not searched for anything"

        return render(request, 'search.html', {'message':message})





