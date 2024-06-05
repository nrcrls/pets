from django.urls import path
from .views import (
    ClientListView,
    ClientDetailView,
)

urlpatterns = [
    path("<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("", ClientListView.as_view(), name="client_list")
]