from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from events.views import showHome
from core.views import NoPermissions,EventureContact,EventureAboutus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',showHome,name="home"),
    path('no-permission/',NoPermissions,name="no-permission"),
    path('',include('events.urls')),
    path('contact/',EventureContact.as_view(),name="contact"),
    path('aboutus/',EventureAboutus.as_view(),name="aboutus"),
    path('users/',include('users.urls')),
]

# Add debug toolbar only in development
if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)