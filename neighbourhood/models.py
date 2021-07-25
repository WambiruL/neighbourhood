from django.db.models.deletion import DO_NOTHING
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from tinymce.models import HTMLField

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    occupants=models.PositiveIntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


    @classmethod
    def find_neighbourhood_by_id(cls, search_term):
        search_results = cls.objects.filter(neighbourhood_name__icontains = search_term)
        return search_results

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self, neighbourhood_name):
        self.neighbourhood_name = neighbourhood_name
        self.save()



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)
    neighbourhood=models.ForeignKey(Neighbourhood,related_name='neighbourhood',on_delete=DO_NOTHING,null=True)

    def __str__(self):
        return f'{self.user} Profile'

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        print("signal activated---->>>", dir(instance))
        instance.profile.save

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(Neighbourhood,related_name='business', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner=models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_business_name(cls, search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

