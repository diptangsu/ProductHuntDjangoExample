from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    else:
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']
        if pass1 == pass2:
            try:
                User.objects.get(username=username)
                return render(request, 'accounts/signup.html',
                              {'error': 'Username already exists. Please pick a different username'})
            except User.DoesNotExist:
                user = User.objects.create_user(username, password=pass1)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Your passwords don\'t match'})


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Incorrect username or password'})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
