from django.urls import path
from . import views


urlpatterns = [
    path('number/all/', views.get_all_numbers, name='get-all-models'),
    path('number/create/', views.insert_number, name='upload-number'),
    path('number/<str:number>/', views.get_specific_number,
         name='get-specific-number')
]
