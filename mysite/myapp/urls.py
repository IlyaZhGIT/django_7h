from django.urls import path

from myapp.views import *

app_name = "myapp"

urlpatterns = [
    path("products/", products, name="products"),
    path("products/<int:my_id>/", product_id, name="details"),
    path("additem/", additem, name="additem.html"),
    path("updateitem/<int:my_id>/", updateitem, name="updateitem"),
    path("deleteitem/<int:my_id>/", deleteitem, name="deleteitem"),
]
