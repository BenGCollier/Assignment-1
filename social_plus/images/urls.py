from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path(
        'detail/<int:id>/<slug:slug>/',
        views.image_detail,
        name='detail',
    ),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
    path('ranking/', views.image_ranking, name='ranking'),


    path('recipe_create/', views.recipe_image_create, name='recipe_create'),
    path(
        'detail/<int:id>/<slug:slug>/',
        views.recipe_image_detail,
        name='recipe_detail',
    ),
    path('recipe_like/', views.recipe_image_like, name='recipe_like'),
    path('', views.recipe_image_list, name='recipe_list'),
    path('recipe_ranking/', views.recipe_image_ranking, name='recipe_ranking'),
]