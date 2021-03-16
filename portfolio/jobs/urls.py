from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('summary/', views.summary, name="summary"),
    path('contact/', views.contact, name='contact'),  
    path('<int:job_id>/', views.detail, name='detail'),  
]