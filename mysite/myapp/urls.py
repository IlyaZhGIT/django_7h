from django.urls import path

from myapp.views import *

app_name = "myapp"

urlpatterns = [
    path("products/", products, name="products"),
    # path("products/", ProductListView.as_view(), name="products"),
    # path("products/<int:my_id>/", product_id, name="details"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="details"),
    path("additem/", additem, name="additem"),
    path("updateitem/<int:my_id>/", updateitem, name="updateitem"),
    path("deleteitem/<int:pk>/", DeleteItem.as_view(), name="deleteitem"),
    path("payment_success/<int:pk>/", PaymentSuccessView.as_view(), name="success"),
    path("payment_failed/<int:pk>/", PaymentFailedView.as_view(), name="failed"),
    path(
        "api/checkout-session/<int:id>/",
        create_checkout_session,
        name="api_checkout-session",
    ),
]
