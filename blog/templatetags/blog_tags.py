from django import template
from ..models import Post,Category

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
    return Category.objects.all()

