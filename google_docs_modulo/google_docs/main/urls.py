from django.urls import path
from main import views

urlpatterns = [
	path("", views.viewConnection, name="index"),
	path("getfiles/",views.getFilesAndMerge, name="url_getfiles")
]