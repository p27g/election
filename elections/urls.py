from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'elections'

urlpatterns = [
                  # /home/
                  url(r'^$', views.home, name='home'),
                  url(r'^templates/hashtags/$', views.hashtags, name='hashtags'),
                  url(r'^templates/retweets/$', views.retweets, name='retweets'),
                  url(r'^templates/popularity/$', views.popularity, name='popularity'),
                  url(r'^templates/location/$', views.location, name='location'),
                  url(r'^templates/analysis/$', views.analysis, name='analysis'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
