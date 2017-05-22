from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^room/$', views.RoomList.as_view()),
    url(r'^room/(?P<room_id>\d+)/$', views.RoomDetail.as_view()),
    url(r'^car/$', views.CarList.as_view()),
    url(r'^car/(?P<car_id>\w+)/$', views.CarDetail.as_view()),
    url(r'^temp_employee/$', views.TempEmployeeList.as_view()),
    url(r'^temp_employee/(?P<temp_emp_id>[A-Z]{2}\d+)/$', views.TempEmployeeDetail.as_view()),
]
