from django.conf.urls import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'create', 'profile_create', name='create-profile'),
    url(r'edir', 'profile_edit', name='edit-profile'),
)
