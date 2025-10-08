from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.core.paginator import Paginator  
from .models import Post, Comment
from .forms import PostForm, CommentForm

def home(request):
    posts = Post.objects.select_related('author').prefetch_related('comments').all()
    
    # Get parameters
    category = request.GET.get('category')
    search_query = request.GET.get('search')
    sort_by = request.GET.get('sort', 'newest')  # Default to newest
    
    # Filter by category
    if category and category != 'all':
        posts = posts.filter(sport_category=category)
    
    # Filter by search
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # Sort posts
    if sort_by == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_by == 'most_commented':
        posts = posts.annotate(comment_count=Count('comments')).order_by('-comment_count')
    else:  # newest (default)
        posts = posts.order_by('-created_at')
    
    # PAGINATION HERE
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get categories
    categories = Post.SPORT_CHOICES
    
    # Calculate community stats
    total_posts = Post.objects.count()
    total_users = User.objects.count()
    total_comments = Comment.objects.count()
    
    
    return render(request, 'home.html', {
        'posts': page_obj,
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category,
        'search_query': search_query,
        'current_sort': sort_by,
        'total_posts': total_posts,
        'total_users': total_users,
        'total_comments': total_comments,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Sports Arena, {user.username}! 🎉')
            return redirect('community:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been published! 🚀')
            return redirect('community:home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.select_related('author'), 
        pk=pk
    )
    
    # Increment view count (only once per session)
    session_key = f'post_{pk}_viewed'
    if not request.session.get(session_key, False):
        post.views += 1
        post.save(update_fields=['views'])
        request.session[session_key] = True
    
    comments = post.comments.select_related('author').all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, 'Comment added successfully! 💬')
                return redirect('community:post_detail', pk=pk)
        else:
            return redirect('login')
    else:
        comment_form = CommentForm()
    
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

def user_profile(request, username):
    """Display user profile with their posts and stats"""
    profile_user = get_object_or_404(User, username=username)
    user_posts_all = Post.objects.filter(author=profile_user).order_by('-created_at')
    user_comments = Comment.objects.filter(author=profile_user).order_by('-created_at')[:5]
    
    # Add pagination for user posts
    paginator = Paginator(user_posts_all, 5)  # 5 posts per page on profile
    page_number = request.GET.get('page')
    user_posts = paginator.get_page(page_number)
    
    # Calculate stats
    total_posts = user_posts_all.count()
    total_comments = Comment.objects.filter(author=profile_user).count()
    
    context = {
        'profile_user': profile_user,
        'user_posts': user_posts,
        'page_obj': user_posts,  # For pagination controls
        'user_comments': user_comments,
        'total_posts': total_posts,
        'total_comments': total_comments,
    }
    return render(request, 'user_profile.html', context)

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('community:post_detail', pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated! 💾')
            return redirect('community:post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('community:post_detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted.')
        return redirect('community:home')
    return render(request, 'delete_confirm.html', {'post': post})

def activity_feed(request):
    """Show recent activity across the community"""
    # Get recent posts
    recent_posts = Post.objects.all().order_by('-created_at')[:10]
    
    # Get recent comments with their posts
    recent_comments = Comment.objects.select_related('post', 'author').order_by('-created_at')[:15]
    
    # Combine and sort by date
    activities = []
    
    for post in recent_posts:
        activities.append({
            'type': 'post',
            'object': post,
            'user': post.author,
            'timestamp': post.created_at,
        })
    
    for comment in recent_comments:
        activities.append({
            'type': 'comment',
            'object': comment,
            'user': comment.author,
            'timestamp': comment.created_at,
        })
    
    # Sort all activities by timestamp
    activities.sort(key=lambda x: x['timestamp'], reverse=True)
    activities = activities[:20]  # Show top 20 activities
    
    return render(request, 'activity_feed.html', {'activities': activities})

@login_required
def delete_comment(request, pk):
    """Delete a comment"""
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    
    # Only allow author to delete
    if comment.author != request.user:
        messages.error(request, 'You can only delete your own comments.')
        return redirect('community:post_detail', pk=post_pk)
    
    comment.delete()
    messages.success(request, 'Comment deleted successfully.')
    return redirect('community:post_detail', pk=post_pk)

def custom_404(request, exception):
    """Custom 404 error handler"""
    return render(request, '404.html', status=404)

def custom_500(request):
    """Custom 500 error handler"""
    return render(request, '500.html', status=500)