from django.conf.urls.defaults import patterns, include, url
from flavyoutube.apps import common
from flavyoutube import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'slogin/?$', 'common.views.login'),
    (r'slogout/?$', 'common.views.logout'),
    (r'^$', 'common.views.index'),
    (r'watch/*', 'common.views.watch'),
    (r'upload/*', 'common.views.upload'),
    
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
    ) 
