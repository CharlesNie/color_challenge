from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from .models import Color, ColorSpace
from .views import ColorSpaceView


class ColorTestCase(TestCase):
    """Test cases for model Color

    To run:
        python manage.py test apps.color_swatch.tests
    """

    def setUp(self):
        Color.objects.create(name="red", min_value=0, max_value=255)
        Color.objects.create(name="green", min_value=0, max_value=255)
        Color.objects.create(name="hue", min_value=0, max_value=360)

    def test_random_value(self):
        for color in Color.objects.all():
            self.assertTrue(color.min_value <= color.random_value <= color.max_value)


class ColorSpaceViewTestCase(APITestCase):
    """Test cases for color space view

    To run:
        python manage.py test apps.color_swatch.tests
    """

    def setUp(self):
        self.min = 0
        self.max = 255
        self.red = Color.objects.create(name="red", min_value=self.min, max_value=self.max)
        self.green = Color.objects.create(name="green", min_value=self.min, max_value=self.max)
        self.blue = Color.objects.create(name="blue", min_value=self.min, max_value=self.max)

        self.rgb = ColorSpace.objects.create(name="rgb")
        self.rgb.colors.add(self.red, self.green, self.blue)

        self.factory = APIRequestFactory()

    def test_color_space_view_response(self):
        request = self.factory.get(reverse('color_spaces'))
        response = ColorSpaceView.as_view()(request)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 5)
        for item in response.data:
            self.assertEqual(item['type'], self.rgb.name)
            colors = item['colors']
            self.assertTrue(self.red.min_value <= colors['red'] <= self.red.max_value)
            self.assertTrue(self.red.min_value <= colors['green'] <= self.red.max_value)
            self.assertTrue(self.red.min_value <= colors['blue'] <= self.red.max_value)
