from django.contrib import admin
from django.urls import path, re_path
from visits.swagger import schema_view

from visits import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r'^get_sale_points/(?P<telephone_number>[0-9]+)/$',
        views.get_sale_points,
        name='get_sale_points'
    ),
    re_path(
        r'^create_visit/(?P<telephone_number>[0-9]+)/$',
        views.create_visit,
        name='create_visit'
    ),
    path(
        'swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
