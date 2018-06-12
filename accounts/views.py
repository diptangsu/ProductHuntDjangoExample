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
    return render(request, 'accounts/')


def logout(request):
    # TODO: need to route to homepage
    pass
