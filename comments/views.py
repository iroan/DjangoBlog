from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk = post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # 关联评论和被评论文章
            comment.post = post
            comment.save()
        else:
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)
