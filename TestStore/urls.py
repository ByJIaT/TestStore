from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from TestStore import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/', include('shopping_cart.urls')),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
