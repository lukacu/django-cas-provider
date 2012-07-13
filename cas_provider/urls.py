from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^login/', login, name="cas_provider_login"),
    url(r'^validate/', validate, name="cas_provider_validate"),
    url(r'^logout/', logout, name="cas_provider_logout"),
)
