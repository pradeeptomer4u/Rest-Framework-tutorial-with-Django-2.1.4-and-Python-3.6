from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include

from todos import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    path('', views.todoListView.as_view(), name="todo_list"),
]



if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)