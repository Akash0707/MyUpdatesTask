from django.urls import path
from . import views


urlpatterns = [


    path('', views.MyclassView.as_view(), name='my-class'),
    path('myfun/', views.hello_world, name='my-fun'),

]
