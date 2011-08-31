# coding: utf-8

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^admin/doc/', include('django.contrib.admindocs.urls')),
  (r'^admin_tools/', include('admin_tools.urls')),
  (r'^admin/', include(admin.site.urls)),
  # home page - elenco attività
  (r'^$', 'website.views.activities_index'),  
  # dettaglio attività
  (r'^scheda/(?P<slug>[-\w]+)/$', 'website.views.activity_detail'),
)

# static assets (not for production!)
if (settings.ENVIRONMENT != 'production'):
  urlpatterns += patterns('',
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '%s/../uploads/' % settings.BASE_DIR}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '%s' % settings.MEDIA_ROOT}),
    (r'^robots.txt$', 'django.views.static.serve', 
      { 'path' : "/robots.txt", 
        'document_root': settings.TEMPLATE_DIRS[0],
        'show_indexes': False } ),
    (r'^favicon.ico$', 'django.views.static.serve', 
      { 'path' : "/favicon.ico", 
        'document_root': settings.TEMPLATE_DIRS[0],
        'show_indexes': False } ),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/css" % settings.TEMPLATE_DIRS[0]}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/images" % settings.TEMPLATE_DIRS[0]}),
    (r'^works/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/works" % settings.TEMPLATE_DIRS[0]}),
    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/fonts" % settings.TEMPLATE_DIRS[0]}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/js" % settings.TEMPLATE_DIRS[0]}),  
  )

  
