from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_recent_posts(num = 5):
    # 这种操作很漂亮啊!!
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.all().dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_post = Count('post')).filter(num_post__gt = 0)

@register.simple_tag
def get_tags():
    # TODO 标签显示不全,显示一个标签相关的全部文章还没有实现
    return Tag.objects.annotate(num_post = Count('post')).filter(num_post__gt = 0)

