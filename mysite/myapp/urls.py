from django.urls import path

from myapp.views import *

app_name = "myapp"

urlpatterns = [
    path("products/", products),
    path("products/<int:my_id>/", product_id, name="details"),
]
