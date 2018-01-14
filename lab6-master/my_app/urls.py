from django.conf.urls import url
from . import views
from my_app.views import hotelview

urlpatterns = [
    url(r'^(?P<id>\d+)', hotelview.as_view(), name='ticket_url'),
]
