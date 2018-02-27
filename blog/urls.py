from django.conf.urls import url
from . import views

<<<<<<< HEAD
=======
app_name = 'blog'
>>>>>>> develop
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail')
]