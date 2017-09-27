
from django.conf.urls import url
from django.contrib import admin
from blog import views
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$', views.index,name='codersarena'),
url(r'^blog/$', views.blogindex,name='base'),
url(r'^blog/view/(?P<post>\d+)', views.view_post, name='view_blog_post'),
url(r'^blog/category/(?P<category>\d+)', views.view_category, name='view_blog_category'),
url(r'^projects/$',views.project)
]
