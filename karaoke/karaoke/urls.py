from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf import settings

from karaoke.app.views import call, response

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r"^call/$", call),
    url(r"^response/$", response),

    # Examples:
    # url(r'^$', 'karaoke.views.home', name='home'),
    # url(r'^karaoke/', include('karaoke.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
               'document_root': settings.STATIC_ROOT,
           }),
)
