from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^articles/', include('article.urls')),
    # url(r'^$', 'testproj.views.home', name='home'),
    # url(r'^testproj/', include('testproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'testproj.views.login'),
    url(r'^accounts/auth/$', 'testproj.views.auth_view'),
    url(r'^accounts/logout/$', 'testproj.views.logout'),
    url(r'^accounts/loggedin/$', 'testproj.views.loggedin'),
    url(r'^accounts/invalid/$', 'testproj.views.invalid_login'),

    url(r'^accounts/register/$', 'testproj.views.register_user'),
    url(r'^accounts/register_success/$', 'testproj.views.register_success'),

)
