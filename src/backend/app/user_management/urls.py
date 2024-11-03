from django.urls import path
from . import user_views

urlpatterns = [
    path('create/', user_views.create_user, name='create_user'),
    path('<int:user_id>/', user_views.get_user, name='get_user'),
    path('<int:user_id>/update/', user_views.update_user, name='update_user'),
    path('<int:user_id>/delete/', user_views.delete_user, name='delete_user'),
]
