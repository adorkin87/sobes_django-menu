from django.urls import path
from . import views


urlpatterns = [
    path('<slug:url_pages>', views.pages),
    path('', views.index, name='home'),
]