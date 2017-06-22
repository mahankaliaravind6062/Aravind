from django.conf.urls import url, include
from django.contrib import admin
from.views import homes

urlpatterns = [
    # Examples:
    # url(r'^$', 'Demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url (r'^$', homes, name="homes"),

]
