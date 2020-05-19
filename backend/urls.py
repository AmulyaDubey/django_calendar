from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('dashboard/<str:pk>/',views.dashboard, name="dashboard"),
    path('create/<str:pk>/', views.create, name="create"),
    path('show/<str:pk>/', views.show, name="show"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('update/<str:pk>/', views.update, name="update"),
    path('update2/<str:pk1>/<str:pk2>', views.update2, name="update2")

]
