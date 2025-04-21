from django.urls import path
from .views import FarePredictionView

urlpatterns = [
    path("predict/", FarePredictionView.as_view(), name="predict_fare"),
]
