from rest_framework.serializers import BaseSerializer
from .models import ColorSpace


class ColorSpaceSerializer(BaseSerializer):
    """Serializing color spaces"""

    def to_representation(self, color_space: ColorSpace):
        data = dict()
        data['type'] = color_space.name
        colors = dict()
        for color in color_space.colors.all():
            colors[color.name] = color.random_value
        data['colors'] = colors
        return data
