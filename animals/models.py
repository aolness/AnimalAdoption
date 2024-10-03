from django.db import models
from django.utils import timezone
from django.urls import reverse
from shelters.models import Shelter


# Create your models here.
class Animal(models.Model):
    date_entered = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100, null=True)
    species = models.ForeignKey('Species', on_delete=models.SET_NULL, blank=False, null=True)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, blank=True, null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, blank=False)
    views = models.IntegerField(default=0)
    availability = models.ForeignKey('Availability', on_delete=models.PROTECT)
    disposition = models.ManyToManyField('Disposition', blank=True)
    size = models.ForeignKey('Size', on_delete=models.PROTECT, blank=True)
    image = models.ImageField(default='placeholder_animal.png', upload_to='animal_pics', blank=True)

    def __str__(self):
        animal_str = f"{self.name} {self.species}, {self.age}"
        return animal_str
    
    def get_absolute_url(self):
        """Returns the url to access a detailed record for this animal"""
        return reverse('animals-detail', args=[str(self.id)])


    class Meta:
        ordering = ['date_entered']


class Species(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "species"


class Breed(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Availability(models.Model):
    availability = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.availability
    
    class Meta:
        verbose_name_plural = "availabilities"


class Disposition(models.Model):
    disposition = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.disposition
