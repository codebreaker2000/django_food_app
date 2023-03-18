from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import register_form
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'welcome {username}, your account has been successfully created')
            return redirect('login')
    else:    
        form=register_form()
    return render(request,'users/register.html',{'form':form})

@login_required
def user_profile(request):
    return render(request,'users/profile.html')

