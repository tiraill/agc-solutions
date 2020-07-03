from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = 'Cайт AGC'
admin.site.site_header = 'Раздел администратора AGC'
admin.site.index_title = 'Раздел администратора AGC'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agc.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
