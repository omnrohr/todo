from django.urls import path
from .views import hello, updatetask
urlpatterns = [
    path('', hello, name= 'tasks'), 
    path('update/<int:pk>/', updatetask, name='update'),
]
