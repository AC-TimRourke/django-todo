from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    # GET /todos
    path('', views.index, name='index'),

    # GET /todos/1
    path('<int:todo_id>', views.todo, name='todo'),

    # PUT /todos/1/update
    path('<int:todo_id>/update/', views.update, name='update'),

    # POST /todos/create
    path('create/', views.create, name='create')
]