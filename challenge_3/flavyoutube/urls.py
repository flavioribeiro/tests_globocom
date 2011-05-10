from django.conf.urls.defaults import patterns, include, url
from flavyoutube.apps import common
from flavyoutube import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'login/?$', 'common.views.log_me_in'),
    (r'logout/?$', 'common.views.log_me_out'),
    (r'^$', 'common.views.index'),
    (r'watch/*', 'common.views.watch'),
    (r'upload/*', 'common.views.upload'),
    (r'subscribe/', 'common.views.subscribe'),
    
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
    ) 
