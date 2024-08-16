from django.urls import path
from app1 import views
urlpatterns=[
    path('sayhi',views.fun1)
]