from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import index

urlpatterns = [
    path("", index, name='career')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)