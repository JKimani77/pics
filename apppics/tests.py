from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,Location, Category

class ImageTestClass(TestCase):
    '''
    Test case for model image
    '''
    def setUp(self):
        self.any_category = Category(name = 'FOOD')
        self.any_location = Location(image_location = 'Bahrain')
        self.any_image = Image(image_name = 'TOMATOES', image_description = 'a tomato tomattoed', image = '/path.image.png', category =self.any_category)


    def test_search_by_category(self):
        self.any_category.save_tag()
        self.any_image.save_image()
        images = self.any_image.search_by_tag('FOOD')
        self.assertTrue(len(images)>0)

class LocationTestClass(TestCase):
    '''
    test case for location model
    '''
    def setUp(self):
        self.any_location = Location(image_location = 'Poland')

    def test_save_location(self):
        self.any_location.save_location()
        any_locations = Location.objects.all()
        self.assertTrue(len(any_locations)>0)
