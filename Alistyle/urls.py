from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from asosiyapp.views import Home2View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home2View.as_view(), name='home2'),
    path('asosiy/', include('asosiyapp.urls')),
    path('user/', include('userapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)