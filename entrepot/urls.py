from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^commodity/$', views.CommodityList.as_view()),
    url(r'^commodity/(?P<commodity_id>\d+)/$', views.CommodityDetail.as_view()),
    url(r'^in_entrepot/$', views.InEntrepotList.as_view()),
    url(r'^in_entrepot/(?P<ie_id>\d+)/$', views.InEntrepotDetailView.as_view()),
    url(r'^out_entrepot/$', views.OutEntrepotList.as_view()),
    url(r'^out_entrepot/(?P<oe_id>\d+)/$', views.OutEntrepotDetailView.as_view()),
]
