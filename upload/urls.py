from django.conf.urls.defaults import *
import views as upload_views
urlpatterns = patterns('',
    url(r'images/$', upload_views.images),
    url(r'files/$', upload_views.files),
    url(r'^$', upload_views.all),
)
