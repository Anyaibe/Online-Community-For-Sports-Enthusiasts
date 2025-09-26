from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log them in
            return redirect('community:home')  # Go to homepage
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save to database yet
            post.author = request.user      # Set the author to current user
            post.save()                     # Now save to database
            return redirect('community:home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})