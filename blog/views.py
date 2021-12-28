from django.shortcuts import render, get_object_or_404
from .models import Blog

def index(request):
    posts = Blog.objects.order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post} )
