from django.shortcuts import render,redirect
from .forms import CreateUserForm

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
    return render(request,'index.html')

