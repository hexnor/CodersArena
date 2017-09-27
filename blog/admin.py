from django.contrib import admin
from blog.models import Blogs, Categories

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body','posted','category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Blogs, BlogAdmin)
admin.site.register(Categories, CategoryAdmin)
