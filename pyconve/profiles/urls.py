from django.conf.urls import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'create/$', 'profile_create', name='create-profile'),
    url(r'success/$', 'profile_success', name='success-profile'),
    url(r'edit/$', 'profile_edit', name='edit-profile'),
    url(r'confirm/(?P<encoded>\.+)/$', 'profile_activate', name='activate-profile'),
)
