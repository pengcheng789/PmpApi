from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^employees/$', views.EmployeeList.as_view()),
    url(r'^employees/(?P<emp_id>[A-Z]{2}\d{4})/$', views.EmployeeDetail.as_view(),
        name='employee-detail'),
    url(r'^news/$', views.NewsList.as_view()),
    url(r'^news/(?P<news_id>\d+)/$', views.NewsDetail.as_view()),
    url(r'^activity/$', views.ActivityList.as_view()),
    url(r'^activity/(?P<act_id>\d+)/$', views.ActivityDetail.as_view()),
]
