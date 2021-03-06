from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    # [0-9]{4}:0到9的数字出现4次
    # [0-9]{1,2}:0到9的数字出现1,2次
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
    url(r'^search/$',views.search,name='search')
]