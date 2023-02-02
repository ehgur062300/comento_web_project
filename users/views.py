from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/home/')

    else :
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})
