from markdown import markdown
from django.shortcuts import render,get_object_or_404
from .models import Post,Category
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown(post.body,extensions = ['markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.toc',
                                                 ])
    return render(request,'blog/detail.html',context={'post':post})

def archives(request,year,month):
    # created_time__month是作为参数的写法,如果是类实例中调用属性方法则用created_time.month
    post_list = Post.objects.filter(created_time__year = year,
                                    created_time__month=month).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    # 参数是一个模型类
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category = cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
