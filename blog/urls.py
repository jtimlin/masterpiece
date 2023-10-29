from . import views
from django.urls import path


urlpatterns = [
    path('', views.PaintingList.as_view(), name='home'),
    path('mypaintings/', views.MyPaintings.as_view(), name='my_paintings'),
    path('addpainting/', views.AddPainting.as_view(), name='add_painting'),
    path('aboutus/', views.AboutUs.as_view(), name='about_us'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('<slug:slug>/update/', views.UpdatePainting.as_view(), name='update_painting'),
    path('<slug:slug>/delete/', views.DeletePainting.as_view(), name='delete_painting'),
    path('comments/<int:pk>/update/', views.UpdateComment.as_view(), name='update_comment'),
    path('comments/<int:pk>/delete/', views.DeleteComment.as_view(), name='delete_comment'),
    path('mylikes/', views.MyLikes.as_view(), name='my_likes'),
    path('like/<slug:slug>', views.LikePainting.as_view(), name='like_painting'),
    path('<slug:slug>', views.PaintingDetail.as_view(), name='painting_detail'),
]
