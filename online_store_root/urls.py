from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from online_store_root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('brand/', include('applications.brand.urls')),
    path('clothes/', include('applications.clothes.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
