from django.urls import path
from todolist.views import deletion, register,login_user, show_todolist,logout_user
from todolist.views import create_task, update

app_name = 'todolist'

urlpatterns = [
    path('',show_todolist, name = 'show_todolist'),
    path('register/', register, name = 'register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task', create_task, name = 'create_task'),
    path('delete-task/<str:id>/', deletion, name = 'deletion'),
    path('update-task/<str:id>/', update, name='update'),
]