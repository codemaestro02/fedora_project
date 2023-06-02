from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import about, index, contact, search


urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("search/", search, name="search"),
    path("contact-us/", contact, name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)