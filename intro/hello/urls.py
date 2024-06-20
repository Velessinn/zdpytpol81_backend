from django.urls import path

from hello import views

urlpatterns = [
    #view intro
    path('', views.hello_view),

    #templates intro
    path('hi/', views.hi_view),
    path('hi2/', views.hi2_view),

    # user input
    path('byk/', views.byk_view),
    #path('<str:name>/', views.name_view),
    path('<str:name>/2/', views.name_view2),

    path('isitnewyear/', views.is_it_new_year),
    path('collection/', views.collection_view),
]

# 3 warstwowa architektura
# warstwa danych
# warstwa logiki
# warstwa prezentacji