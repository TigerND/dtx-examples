from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/say/(?P<message>.*)/',
        'hello.views.say'
    ),
    url(r'^hello/',
        'hello.views.say',
    	{ 'message': 'Hello World!!!'
    	}
    ),
)
