from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^repair/$', views.RepairListView.as_view()),
    url(r'^repair/(?P<repair_id>\d+)/$', views.RepairDetail.as_view()),
]
