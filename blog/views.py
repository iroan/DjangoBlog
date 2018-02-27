<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render,get_object_or_404
>>>>>>> develop
from .models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
<<<<<<< HEAD
=======

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',context={'post':post})
>>>>>>> develop
