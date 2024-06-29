from django.shortcuts import render
from .models import Post

from django.shortcuts import render, get_object_or_404 #now this has been imported


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts' : posts})

def post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    #posts = Post.objects.get(id=pk) and this has been commented out
    return render(request, 'posts.html', {'posts' : posts})