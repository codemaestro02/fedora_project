from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import about, index


urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)