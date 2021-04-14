from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from core.models import Tweet, HashTag
from django.contrib.auth.models import User

def splash(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        body = request.POST['body']
        Tweet.objects.create(body=body, author=request.user)
    tweets = Tweet.objects.filter(author=request.user)
    return render(request, 'splash.html', {'tweets': tweets})

def like_home(request):
  if request.method == "POST":
    like_id = request.POST["like_id"]
    tweet = Tweet.objects.get(id=like_id)
    if tweet.likes.filter(id=request.user.id).exists():
      tweet.likes.remove(request.user)
    else:
      tweet.likes.add(request.user)
    return redirect('/home')

def like(request):
  if request.method == "POST":
    like_id = request.POST["like_id"]
    tweet = Tweet.objects.get(id=like_id)
    if tweet.likes.filter(id=request.user.id).exists():
      tweet.likes.remove(request.user)
    else:
      tweet.likes.add(request.user)
    return redirect('/profile/' + request.user.username)

def profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        body = request.POST['body']
        if len(body) == 0:
            author_user = User.objects.get(username=username)
            tweets = Tweet.objects.filter(author=author_user)
            return render(request, 'profile.html', {'tweets': tweets, 'username': username})
        words = body.split()
        tags = [word[1:] for word in body.split() if word[0] == "#" and len(word) > 1]
        tweet = Tweet.objects.create(body=body, author=request.user)
        for tag in tags:
            if not HashTag.objects.filter(tag=tag).exists():
                HashTag.objects.create(tag=tag)
            htag = HashTag.objects.filter(tag=tag)[0]
            tweet.hashtags.add(htag)
    author_user = User.objects.get(username=username)
    tweets = Tweet.objects.filter(author=author_user)
    return render(request, 'profile.html', {'tweets': tweets, 'username': username})

def hashtag_home(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    hashtags = HashTag.objects.all()
    return render(request, 'hashtag.html', {'hashtags': hashtags})

def hashtag_view(request, hashtag):
    if not request.user.is_authenticated:
        return redirect('/login') 
    tweets = Tweet.objects.filter(hashtags__tag=hashtag)
    hashtags = HashTag.objects.filter(tag=hashtag)
    return render(request, 'hashtag.html', {'hashtags': hashtags, 'tweets': tweets})

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        body = request.POST['body']
        Tweet.objects.create(body=body, author=request.user)
    tweets = Tweet.objects.all()
    hashtags = HashTag.objects.all()
    return render(request, 'home.html', {'tweets': tweets, 'hashtags': hashtags})

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

def delete_home(request): 
    tweet = Tweet.objects.get(id=request.GET['id'])
    tweet.delete()
    path = '/home'
    return redirect(path)