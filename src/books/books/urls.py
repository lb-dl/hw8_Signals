from user import views as uv

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cu/', uv.creat_users, name='user-create'),
    path('ul/', uv.users, name='user-name'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('uu/<int:pk>/', uv.update_user, name='user-update'),
]
