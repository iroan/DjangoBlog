from django.contrib import admin
<<<<<<< HEAD
from .models import Category,Tag,Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)

=======
from blog.models import Post
from blog.models import Category
from blog.models import Tag
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
>>>>>>> develop
