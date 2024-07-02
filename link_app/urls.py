from django.urls import path

from link_app import views

app_name = 'link_app'

urlpatterns = [
    path('first/', views.first_view, name='first'),
    path('drugi/', views.second_view, name='second'),
    path('third/<str:param>/', views.third_view, name='third'),

]