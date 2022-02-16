from django.urls import path

from . import views

app_name = 'cdp'


urlpatterns = [
    
    # site
    path('<str:api_version>/view/', views.record_view_event, name="tracking_view"),
    path('<str:api_version>/click/', views.record_click_event, name="tracking_click"),

    # mdeia
]
