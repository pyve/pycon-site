from django.conf.urls import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'create/$', 'profile_create', name='create-profile'),
    url(r'success/$', 'profile_success', name='success-profile'),
    url(r'edit/$', 'profile_edit', name='edit-profile'),
    url(r'confirm/(?P<encoded>\.+)/$', 'profile_activate', name='activate-profile'),
    url(r'speaker/register/$', 'speaker_registration', name='speaker-registration'),
    url(r'me/$', 'profiles_myprofile', name='my-profile'),
    url(r'logout/$', 'logout', name='logout'),
)

urlpatterns += patterns('',
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'login.html'},name='profiles-login'),
)
