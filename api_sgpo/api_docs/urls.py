from django.urls import path
from . import views

urlpatterns = [
	path('connection/', views.viewConnection),
	path('gerarDocumento/', views.getFilesAndMerge)
]
