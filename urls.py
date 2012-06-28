from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    # Examples:
    # url(r'^$', 'regqs.views.home', name='home'),
    # url(r'^regqs/', include('regqs.foo.urls')),
      url(r'^accounts/', include('registration.urls')),
      url(r'^admin/', include(admin.site.urls)),
      url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 
'registration/login.html'}),
)
