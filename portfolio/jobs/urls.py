from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('summary/', views.summary, name="summary"),
    path('contact/', views.contact, name='contact'),  
    path('blog/', views.blog, name='blog'),
    path('user/', views.user, name='user'),
    path('edit_user/<int:user_id>/update', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/delete', views.delete_user, name='delete_user'),
    path('<int:job_id>/', views.detail, name='detail'),  
]