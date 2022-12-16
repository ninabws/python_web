from django.urls import path
from . import views

urlpatterns = [
	path("",views.index, name="index"),
	path("ninaN",views.nina, name="index2"),
	path("maryaneM",views.maryane, name="index3"),
	path("<str:name>", views.greet, name="greet")
]
