from django.urls import path

<<<<<<< HEAD
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]
=======
app_name = 'users'

urlpatterns = []
>>>>>>> ff21b459de8db17bb1bb0512dad38e2e6cb193ca
