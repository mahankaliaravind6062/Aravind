from django.conf.urls import url
from django.contrib import admin
from.views import homes

urlpatterns = [
    # Examples:
    # url(r'^$', 'Demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
   # url (r'^$/', homes, name='home'),

]
