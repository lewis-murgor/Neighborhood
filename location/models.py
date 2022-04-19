from django.db import models
from django.contrib.auth.models import User

# Create your models here.
JOIN_CHOICE = (
    ('Join', 'Join'),
    ('Leave', 'Leave'),
)

class Neighborhood(models.Model):
    name = models.CharField(max_length =100)
    location = models.CharField(max_length =60)
    occupants_count = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    health_contact = models.IntegerField()
    police_contact = models.IntegerField()
    joins = models.ManyToManyField(User,blank=True,related_name='joins')

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    def update_neighborhood(self,updated_neighborhood):
        self.neighborhood = updated_neighborhood
        self.save()

    def update_occupants(self,updated_occupants):
        self.occupants = updated_occupants
        self.save()

    @classmethod
    def find_neighborhood(cls,id):
        neighborhood = cls.objects.filter(id = id)
        return neighborhood

class Business(models.Model):
    name = models.CharField(max_length =100)
    image = models.ImageField(upload_to = 'photos/',default='default.png')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self,updated_business):
        self.business = updated_business
        self.save()

    @classmethod
    def find_business(cls,id):
        business = cls.objects.filter(id = id)
        return business

    @classmethod
    def search_by_name(cls,name):
        business = cls.objects.filter(name__icontains=name)
        return business

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'photos/')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self, updated_profile):
        self.profile = updated_profile
        self.save()

class Post(models.Model):
    name = models.CharField(max_length =100)
    photo = models.ImageField(upload_to = 'photos/',null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    value = models.CharField(choices=JOIN_CHOICE,default='Join',max_length=10)

    def __str__(self):
        return self.neighborhood