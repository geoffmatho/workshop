from django.urls import path
from . import views

urlpatterns = [
    path('', views.workshop_list, name='workshop_list'),
    path('workshop/<int:id>/', views.workshop_detail, name='workshop_detail'),
    path('workshop/new/', views.workshop_propose, name='workshop_propose'),
]
