from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('home',views.home),
    path('people', views.get_people),
    path('people/', views.get_people),
    path('people/<int:id>', views.get_people),
    path('people/<int:id>/', views.get_people),
    #Ministry
    path('ministries', views.ministry_endpoint),
    path('ministries/', views.ministry_endpoint),
    path('ministries/<int:id>', views.ministry_endpoint),
    path('ministries/<int:id>/', views.ministry_endpoint),

    #Mustard Seed
    path('mustardseeds/', views.mustard_seed_endpoint),
    path('mustardseeds', views.mustard_seed_endpoint),
    path('mustardseeds/<int:id>', views.mustard_seed_endpoint),
    path('mustardseeds/<int:id>/', views.mustard_seed_endpoint),
]