from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('singup/', views.SingUpView.as_view(), name='sing_up'),
   
]