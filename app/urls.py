from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', RedirectView.as_view(url='cats/list/')),
	path('cats/', include('cats.urls')),
	path('colonies/', include('colonies.urls')),
	path('downloads/', include('downloads.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
	urlpatterns.append( path('__reload__/', include('django_browser_reload.urls')) )
