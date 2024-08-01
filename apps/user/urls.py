from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
     path('logout/', logout_view, name='logout'),
]