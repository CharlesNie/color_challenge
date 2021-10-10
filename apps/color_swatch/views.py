from random import randint
from django.views import View
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import ColorSpace
from .serializers import ColorSpaceSerializer


class ColorSpaceView(ListAPIView):
    """View for serving color spaces

    Methods:
        GET: to retrieve color spaces
    """

    queryset = ColorSpace.objects.all()
    serializer_class = ColorSpaceSerializer

    def list(self, request, *args, **kwargs):
        color_spaces = list(self.get_queryset())
        # remove color space with no colors
        color_spaces = list(filter(lambda color_space: len(color_space.colors.all()) > 0, color_spaces))
        total_color_spaces = len(color_spaces)
        if total_color_spaces == 0:
            return Response()
        elif total_color_spaces < 5:
            color_spaces.extend([
                color_spaces[randint(0, total_color_spaces - 1)] for _ in range(5 - total_color_spaces)
            ])
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(color_spaces, many=True)
        return Response(serializer.data)


class ColorSwatchView(View):
    """View for presenting color swatch UI
    """

    def get(self, request, *args, **kwargs):

        return render(request, 'color_swatch.html', context={})
