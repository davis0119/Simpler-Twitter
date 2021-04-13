from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from core.models import Tweet
from django.contrib.auth.models import User

def splash(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        body = request.POST['body']
        Tweet.objects.create(body=body, author=request.user, likes=0)
    tweets = Tweet.objects.filter(author=request.user)
    return render(request, 'splash.html', {'tweets': tweets})

def profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        body = request.POST['body']
        Tweet.objects.create(body=body, author=request.user, likes=0)
    author_user = User.objects.get(username=username)
    tweets = Tweet.objects.filter(author=author_user)
    return render(request, 'profile.html', {'tweets': tweets, 'username': username})

def hashtag_view(request, hashtag):
    if not request.user.is_authenticated:
        return redirect('/login') 
    tweets = Tweet.objects.filter(hashtags=hashtag)
    return render(request, 'hashtag.html', {'tweets': tweets, 'hashtag': hashtag})

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        body = request.POST['body']
        Tweet.objects.create(body=body, author=request.user, likes=0)
    tweets = Tweet.objects.all()
    return render(request, 'home.html', {'tweets': tweets})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/') 
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect('/login?error=failure')
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html')

def signup_view(request):
    if request.method == 'POST':
        username, password, email = request.POST['username'], request.POST['password'], request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def delete(request): 
    tweet = Tweet.objects.get(id=request.GET['id'])
    tweet.delete()
    path = '/profile/' + str(request.user)
    return redirect(path)