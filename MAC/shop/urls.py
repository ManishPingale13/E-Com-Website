from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("checkout/",views.checkout,name="Checkout"),
    path("product/<int:myId>",views.productView,name="ProductView"),
    path("search/",views.search,name="Search"),
    path("tracker/",views.tracker,name="Tracker"),
    path("contact/",views.contact,name="ContactUs"),
    path("about/",views.about,name="AboutUs")
]
