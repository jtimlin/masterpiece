from . import views
from django.urls import path


urlpatterns = [
    path('', views.PaintingList.as_view(), name='home'),
    path('<slug:slug>/', views.PaintingDetail.as_view(), name='painting_detail'),
    path('like/<slug:slug>', views.LikePainting.as_view(), name='like_painting'),
]
