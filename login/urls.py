from django.conf.urls import url

from login import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^daily/$', views.DailyList.as_view()),
    url(r'^daily/(?P<daily_id>\d+)/$', views.DailyDetail.as_view()),
]
