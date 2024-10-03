from django.contrib import admin
from .models import Animal, Species, Breed, Size, Availability, Disposition


# Register your models here.
admin.site.register(Animal)
admin.site.register(Species)
admin.site.register(Breed)
admin.site.register(Size)
admin.site.register(Availability)
admin.site.register(Disposition)
