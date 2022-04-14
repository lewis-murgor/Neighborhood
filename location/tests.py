from django.test import TestCase
from .models import Neighborhood,Business

# Create your tests here.

class NeighborhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.naiberi=Neighborhood(name='Naiberi',location='Eldoret',occupants_count=200,health_contact=234,police_contact=911)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.naiberi,Neighborhood))

    # Testing Save Method
    def test_create_neighborhood(self):
        self.naiberi.create_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)

    # Testing Delete Method
    def test_delete_neighborhood(self):
        self.naiberi.create_neighborhood()
        self.naiberi.delete_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)

    def test_find_neighborhood(self):
        neighborhood = Neighborhood.find_neighborhood(1)
        self.assertTrue(len(neighborhood) == 0)

class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Creating a new neighborhood and saving it
        self.naiberi=Neighborhood(name='Naiberi',location='Eldoret',occupants_count=200,health_contact=234,police_contact=911)
        self.naiberi.create_neighborhood()

        self.new_business=Business(name='game-house',neighborhood=self.naiberi,email='kiplagatlewis29@gmail.com')
        self.new_business.create_business()

    def tearDown(self):
        Neighborhood.objects.all().delete()
        Business.objects.all().delete()

     # Testing  instance
    def test_check_instance_variables(self):
        self.assertEqual(self.new_business.name, 'game-house')
        self.assertEqual(self.new_business.neighborhood, self.naiberi)
        self.assertEqual(self.new_business.email, 'kiplagatlewis29@gmail.com')

    # Testing Save Method
    def test_create_business(self):
        self.new_business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    # Testing Delete Method
    def test_delete_business(self):
        self.new_business.create_business()
        self.new_business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

    def test_find_business(self):
        business = Business.find_business(1)
        self.assertTrue(len(business) == 0)
