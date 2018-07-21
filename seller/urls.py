from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from seller.api import views
from . import views as v
app_name = "seller"

urlpatterns = [

    #seller/api/sellerlist
    url(r'^api/sellerlist/$', views.sellerList.as_view()),

    #seller/api/sellerdetails/2
    url(r'^api/sellerdetails/(?P<pk>[0-9]+)/$', views.sellerDetail.as_view()),

    #seller/testview
    url(r'^testview/$', v.testview),
]

urlpatterns = format_suffix_patterns(urlpatterns)





