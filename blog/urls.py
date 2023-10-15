from . import views
from django.urls import path


urlpatterns = [
    path('', views.PaintingList.as_view(), name='home'),
]
