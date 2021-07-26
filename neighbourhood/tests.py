from django.test import TestCase
from .models import *

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighbourhood(neighbourhood='lanet')

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Neighbourhood))

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.hood.save_neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.hood.delete_neighbourhood('Lanet')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(business_name='Mama Mboga')

    def test_hood_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business_method(self):
        self.business.save_business()
        business_object = Business.objects.all()
        self.assertTrue(len(business_object) > 0)

    def test_delete_business_method(self):
        self.business.save_business()
        business_object = Business.objects.all()
        self.business.delete_business()
        business_object = Business.objects.all()
        self.assertTrue(len(business_object) == 0)

    def test_search_by_business_name(self):
        business = Business.search_image('fashion')
        self.assertTrue(len(business)>0)
