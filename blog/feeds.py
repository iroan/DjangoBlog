from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    # TODO 功能未完成
    title = 'Demo王凯旋的博客'
    link = '/'
    description = 'Demo王凯旋的博客的测试文章'
    def item(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s]%s' % (item.category,item.title)

    def item_description(self, item):
        return item.body