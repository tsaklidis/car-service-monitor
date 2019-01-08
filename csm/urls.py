from django.conf.urls import url, include
from django.contrib import admin


admin.site.site_header = 'Car Service Monitor (ROOT PANEL)'
admin.site.site_title = 'Super root'

urlpatterns = [
    url(r'panel/', include('csm.panel.urls', 'panel')),
    url(r'', include('csm.public.urls', 'public')),

    url(r'^user/', include('csm.users.urls', 'users')),
    url(r'^admin/', admin.site.urls),
]
