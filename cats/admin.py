from django.contrib import admin
from .models import Cat, Breed
# Register your models here.
admin.site.register(Breed)
admin.site.register(Cat)