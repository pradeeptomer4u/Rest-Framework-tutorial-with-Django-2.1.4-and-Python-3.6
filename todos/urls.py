from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include
from todos import views

app_name = 'todos'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^create/$', views.todoCreateView.as_view(), name="todo_create"),
    re_path(r'^list/$', views.todoListView.as_view(), name="todo_list"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.todoDetailView.as_view(), name="todo_detail"),
    re_path(r'^update/(?P<pk>\d+)/$', views.todoUpdateView.as_view(), name="todo_update"),
    re_path(r'^delete/(?P<pk>\d+)/', views.delete_element,name='delete_element'),]
