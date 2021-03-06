from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('download.views',
    url(r'^search/$', 'search', {'initial-query':''}, name='search'),
    url(r'^search/(?P<initial_query>(\w|.)*)/$', 'search', name='search-initial'),
    url(r'^search/query/$', 'query', name='query'),
    url(r'^get/(?P<filename>(\w|.)+)/', 'getfile', name='getfile')
    # url(r'^simplebx/', include('simplebx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
