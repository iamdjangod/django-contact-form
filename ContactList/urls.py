from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from contact import views
from django.conf.urls.static import static


urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^contact/', include('contact.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)