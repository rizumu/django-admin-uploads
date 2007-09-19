from django.conf.urls.defaults import *
import views as upload_views
urlpatterns = patterns('',
    url(r'download/$', upload_views.download),
    url(r'youtube/$', upload_views.youtube),
    url(r'flickr/$', upload_views.flickr),
    url(r'images/$', upload_views.images),
    url(r'files/$', upload_views.files),
    url(r'^$', upload_views.all),
)
