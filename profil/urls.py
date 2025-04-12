from django.urls import path
from .views import *

app_name = 'profil'
urlpatterns = [
    path('register/', register, name='register'),
    path('profil/', profile, name='profil'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profil'),
    path('s_detail/<int:id>', s_prof, name='s_detail'),
    path('chat/<int:id>/', chat_view, name='chat'),
    path('xabar_tahrir/<int:id>/', edit_message, name='edit_message'),
    path('xabar_ochirish/<int:id>/', delete_message, name='delete_mes'),
    path('confirm_delete/<int:id>/', confirm_delete, name='confirm_delete'),
    path('chatlar/', chat_list, name='chat_list'),

]
