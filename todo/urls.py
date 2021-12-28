from django.urls import path
from .views import deletetask, hello, updatetask
urlpatterns = [
    path('', hello, name= 'tasks'), 
    path('update/<int:pk>/', updatetask, name='update'),
    path('delete/<int:pk>/', deletetask, name='delete'),
]
