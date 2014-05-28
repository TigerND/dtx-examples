from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gittip/info/(?P<username>.*)/',
        'example.views.info'
    ),
    url(r'^gittip/info/',
        'example.views.info',
    	{ 'username': None
    	}
    ),
)
