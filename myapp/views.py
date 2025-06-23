from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Category, Thread, Post
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CustomUserCreationForm()

    return render(request, 'myapp/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'myapp/profile.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'myapp/category_list.html', {'categories': categories})

def thread_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    threads = category.threads.all().order_by('-created_at')
    return render(request, 'myapp/thread_list.html', {'category': category})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = thread.posts.filter(parent__isnull=True).order_by('created_at')  
    return render(request, 'myapp/thread_detail.html', {'thread': thread, 'posts': posts})

@login_required
def create_thread(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        thread = Thread.objects.create(
            title=title,
            category=category,
            author=request.user,
            created_at=timezone.now()
        )
        Post.objects.create(
            thread=thread,
            author=request.user,
            content=content
        )        
        return redirect('thread_detail', thread_id=thread.id)
    return render(request, 'myapp/create_thread.html', {'category': category})

@login_required
def reply_post(request, post_id):
    parent = get_object_or_404(Post, id=post_id)

    # Let me Check if the thread is locked
    if parent.thread.is_locked:
        messages.error(request, "This thread is locked. You can't reply.")
        return redirect('thread_detail', thread_id=parent.thread.id)

    if request.method == 'POST':
        content = request.POST['content']
        Post.objects.create(
            thread=parent.thread,
            author=request.user,
            content=content,
            parent=parent,
            created_at=timezone.now()
        )
        return redirect('thread_detail', thread_id=parent.thread.id)

    return render(request, 'myapp/reply_post.html', {'parent': parent})

@login_required
def report_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.is_reported = True
    post.save()
    messages.success(request, "Post reported to Moderators.")
    return redirect('thread_detail', thread_id=post.thread.id)


def debug_template(request):
    return render(request, 'myapp/thread_list.html')

def search(request):
    query = request.GET.get('q', '')
    threads = Thread.objects.filter(
        Q(title__icontains=query) | Q(posts__content__icontains=query)
    ).distinct()
    return render(request, 'myapp/search_results.html', {'query':query, 'threads' : threads})

@login_required
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.upvotes += 1
    post.save()
    return redirect('thread_detail', thread_id=post.thread.id)

@login_required
def downvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.downvotes += 1
    post.save()
    return redirect('thread_detail', thread_id=post.thread.id)
