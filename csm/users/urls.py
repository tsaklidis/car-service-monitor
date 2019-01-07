from django.conf.urls import url
from django.contrib.auth import views as auth_views

from csm.users.forms import LoginAuthenticationForm


urlpatterns = [
    # Private area "/user" is difined at main urls.py
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'users/login.html',
         'authentication_form': LoginAuthenticationForm},
        name='auth_login'),
    url(r'^logout/$',
        auth_views.logout, {'template_name': 'users/logout.html'},
        name='auth_logout'),
    # url(r'^password/change/$',
    #     'views.password_change',
    #     name='password_change'),
]
