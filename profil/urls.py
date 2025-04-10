from django.urls import path
from .views import *

app_name = 'profil'
urlpatterns = [
    path('register/', register, name='register'),
    path('profil/', profile, name='profil'),
    path('login/', CustomLoginview.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profil'),
    path('s_detail/<int:id>', s_prof, name='s_detail'),
    path('xabar_wr/<int:id>/', xabar_wr, name='xabar_wr'),


]
