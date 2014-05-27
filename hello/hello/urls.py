from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/say/(?P<message>.*)/',
        'hello.views.say'
    ),
    url(r'^hello/say/',
        'hello.views.say',
    	{ 'message': 'Hello World!!!'
    	}
    ),
    url(r'^hello/gw2test/(?P<item_id>.*)/',
        'hello.views.gw2test'
    ),
    url(r'^hello/gw2test/',
        'hello.views.gw2test',
        { 'item_id': 28445
        }
    ),
)
