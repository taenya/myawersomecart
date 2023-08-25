
from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="Shophome"),
   path("about/",views.about,name="AboutUs"),
   path("contact/",views.contact,name="ContactUs"),
   path("tracker/",views.tracker,name="TrackingStatus"),
   path("search/",views.search,name="Search"),
   path("productView",views.productView,name="Search"),
   path("checkout",views.checkout,name="Checkout"),
   path("",views.index,name="Shophome"),
   path("",views.index,name="Shophome"),
]
