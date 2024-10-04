from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap, RecipeSitemap
from . import views
from django.contrib.auth import views as auth_views
from .feeds import LatestPostsFeed, LatestRecipesFeed
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

sitemaps = {
    'posts': PostSitemap,
    'recipes': RecipeSitemap,
}

urlpatterns = [
    # Post views
    path('posts/', views.post_list, name='post_list'),
    path(
        'posts/tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'
    ),
    path(
        'posts/<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail',
    ),
    path('posts/<int:post_id>/share/', views.post_share, name='post_share'),
    path(
        'posts/<int:post_id>/comment/', views.post_comment, name='post_comment'
    ),
    path('posts/feed/', LatestPostsFeed(), name='post_feed'),
    path('posts/search/', views.post_search, name='post_search'),

    # Recipe views
    path('recipes/', views.recipe_list, name='recipe_list'),
    path(
        'recipes/tag/<slug:tag_slug>/', views.recipe_list, name='recipe_list_by_tag'
    ),
    path(
        'recipes/<int:year>/<int:month>/<int:day>/<slug:recipe>/',
        views.recipe_detail,
        name='recipe_detail',
    ),
    path('recipes/<int:recipe_id>/share/', views.recipe_share, name='recipe_share'),
    path(
        'recipes/<int:recipe_id>/comment/', views.recipe_comment, name='recipe_comment'
    ),
    path('recipes/feed/', LatestRecipesFeed(), name='recipe_feed'),
    path('recipes/search/', views.recipe_search, name='recipe_search'),

    # Sitemap view for both posts and recipes
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

    path('login/', auth_views.LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/registration/logout.html'), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='blog/registration/password_change_form.html'
    ), name='password_change'),
    
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='blog/registration/password_change_done.html'
    ), name='password_change_done'),

    path(
        'password-reset/', auth_views.PasswordResetView.as_view(
            template_name='blog/registration/password_reset_form.html'),
        name='password_reset'
    ),
    path(
        'password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='blog/registration/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='blog/registration/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='blog/registration/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    path('', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
]

if settings.DEBUG:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
    )
