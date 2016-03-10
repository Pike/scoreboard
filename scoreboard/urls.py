from django.conf.urls import include, url
from django.contrib import admin

import scoreboard.framework.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'scoreboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(scoreboard.framework.urls)),
]
