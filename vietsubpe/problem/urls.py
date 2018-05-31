from django.urls import path

from . import views

app_name = 'problem'

urlpatterns = [
    path('', views.Home, name='home'),
    path('problem/<int:problem_id>/', views.problem, name='problem')
]
