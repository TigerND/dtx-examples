from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gratipay/info/(?P<username>.*)/',
        'example.views.info'
    ),
    url(r'^gratipay/info/',
        'example.views.info',
    	{ 'username': None
    	}
    ),
    url(r'^gratipay/update/',
        'example.views.update'
    ),
)
