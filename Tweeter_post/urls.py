from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views 



urlpatterns = [
    path("admin/", admin.site.urls),
    path("tweet/", include("tweet.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # Add Django authentication
    path("", RedirectView.as_view(url="/tweet/")),  # Redirect root to /tweet/
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
