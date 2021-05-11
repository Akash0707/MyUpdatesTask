from django.contrib import admin
from django.urls import path
from curdapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentAPI.as_view()),
]
