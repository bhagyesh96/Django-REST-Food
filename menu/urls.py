from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from menu.api import views

app_name="menu"
urlpatterns = [
    #menu/
    url(r'^$', views.menuList.as_view(), name='list'),

    #menu/api/detail/2/
    url(r'^api/detail/(?P<pk>[0-9]+)/$', views.menuDetail.as_view(), name='detail')
]


urlpatterns = format_suffix_patterns(urlpatterns)




