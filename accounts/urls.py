from .views import ProfileDetailView, ProfileUpdateView, ProfileDeleteView
from django.conf.urls.static import static
from django.conf import settings
from .views import SignUp
from django.urls import path


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profileedit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profiledelete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)