from django.urls import path
from . views import abouts_list

app_name = 'aboutus'

urlpatterns = [
    path('abouts/', abouts_list, name='aboutus_list')
    
]



