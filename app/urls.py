from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, AboutPageView
from .views import MemorialListView,MemorialDetailView, MemorialCreateView, MemorialUpdateView, MemorialDeleteView
from .views import AddPhotoView, PhotoUpdateView, PhotoDeleteView
from .views import MessageCreateView, MessageUpdateView, MessageDeleteView


urlpatterns =[

    path('', HomePageView.as_view(), name ='home'),

    path('about/', AboutPageView.as_view(), name ='about'),

    # Memorial
    path('Memorial/', MemorialListView.as_view(), name ='Memorial'),
    path('Memorial/create', MemorialCreateView.as_view(), name ='Memorialcreate'),
    path('Memorial/<int:pk>/edit/', MemorialUpdateView.as_view(), name='Memorialupdate'),
    path('Memorial/<int:pk>/', MemorialDetailView.as_view(), name ='Memorialdetail'),
    path('Memorial/<int:pk>/delete', MemorialDeleteView.as_view(), name='Memorialdelete'),

    # Photo
    path('Memorial/<int:pk>/Photos/', AddPhotoView.as_view(), name='addphoto'),
    path('Memorial/<int:memorial_pk>/Photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='Photoupdate'),
    path('Memorial/<int:memorial_pk>/Photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='Photodelete'),

    #Message
    path('Memorial/<int:pk>/Message', MessageCreateView.as_view(), name='Messagecreate'),
    path('Memorial/<int:memorial_pk>/Message/<int:pk>/update', MessageUpdateView.as_view(), name='Messageupdate'),
    path('Memorial/<int:memorial_pk>/Message/<int:pk>/delete', MessageDeleteView.as_view(), name='Messagedelete'),



     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




