from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from blog.views import post_by_category

def register(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username Taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username,
                                                first_name=first_name,
                                                email=email,
                                                password=password1,
                                                last_name=last_name)
                user.save()
                print('User Created!')
        else:
            print('password not match')
        return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('wrong logins')
            return redirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')