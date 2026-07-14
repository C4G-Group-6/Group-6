from django.urls import path
from django.contrib.auth.views import LogoutView  # <-- Added this import

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),  # <-- Added this line
    path('favorites/add/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/', views.remove_from_favorites, name='remove_from_favorites'),
]