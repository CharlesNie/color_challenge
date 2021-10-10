from django.urls import path
from .views import ColorSpaceView, ColorSwatchView


urlpatterns = [
    path("", ColorSwatchView.as_view(), name="index"),
    path("color-spaces", ColorSpaceView.as_view(), name="color_spaces")
]
