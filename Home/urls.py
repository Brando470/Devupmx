
from django.urls import path
from Home.views import inicio



urlpatterns = [

    path('Devup/',inicio, name='inicio'),

]