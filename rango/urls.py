from django.conf.urls import url
from rango import views
from django.conf import settings
from django.config.urls.static import static 
urlpatterns = [
     url(r'^$', views.index, name='index'),

	 ] + static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)

	 