from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'scoreboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^([a-zA-Z\-]+)$', views.locale_issues),
]
