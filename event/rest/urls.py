from django.conf.urls import include, url
import views


urlpatterns = [
    url(
        r'^blocked_domains/$',
        views.BlockedDomains.as_view(),
        name='blocked_domains'
    ),

]