from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView, AboutPageView, BlogListView,
                    BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, AddPhotoView)

urlpatterns =[

    path('', HomePageView.as_view(), name ='home'),
    path('blogs/', BlogListView.as_view(), name ='blogs'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name ='blogsdetail'),
    path('blogs/create', BlogCreateView.as_view(), name ='blogscreate'),
    path('blogs/<int:pk>/edit/', BlogUpdateView.as_view(), name ='blogsupdate'),
    path('blogs/<int:pk>/delete', BlogDeleteView.as_view(), name='blogsdelete'),
    path('about/', AboutPageView.as_view(), name ='about'),
    path('memorial/<int:pk>/addphoto/', AddPhotoView.as_view(), name='addphoto'),


     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



