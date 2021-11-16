from django.urls import path

from . import views

app_name = 'tracking'


urlpatterns = [
    # email
    path('view/', views.record_view_event, name="tracking_view"),
    path('click/', views.record_click_event, name="tracking_click"),

]
