from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    #path("group/<slug>/", views.group_posts, name="group"),
    path("new/", views.new_post, name="new_post"),
    # Профайл пользователя
    #path("follow/", views.follow_index, name="follow_index"),
    path("<username>/", views.profile, name="profile"),
    # Просмотр записи
    path("<username>/<int:recipe_id>/", views.recipe_view, name="recipe_view"),
    path('recipe/<int:recipe_id>/edit', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:recipe_id>/delete', views.recipe_delete, name='recipe_delete'),
    #path("<username>/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    #path("<username>/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    #path("<username>/follow", views.profile_follow, name="profile_follow"), 
    #path("<username>/unfollow", views.profile_unfollow, name="profile_unfollow"),

]
