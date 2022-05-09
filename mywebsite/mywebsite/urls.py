
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('bootstrap.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)