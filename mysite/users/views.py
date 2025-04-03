from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import Registerform
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcom {username}, your account is created')
            return redirect('login')
    else:
        form = Registerform()
    return render(request , 'users/register.html', {'form': form}) 

