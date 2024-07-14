from django.urls import path, include
from . import views

app_name = "friend"

urlpatterns = [
    path('',  views.index, name='index'),
    path('add/',  views.add, name='add'),
    path('delete/',  views.delete, name='del'),

    path('pending/', views.pending, name='pending'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('refuse/<int:id>', views.refuse, name='refuse'),

    path('list/', views.list, name='list'),
]
