from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.index),
  path('store/<str:device_id>/', views.store, name='store'),
]