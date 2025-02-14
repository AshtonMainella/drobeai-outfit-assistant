# models.py in the wardrobe app

from django.db import models
from django.contrib.auth.models import User

# Define fixed choices for clothing categories
CATEGORY_CHOICES = [
    ('top', 'Top'),
    ('bottom', 'Bottom'),
    ('shoes', 'Shoes'),
]

class ClothingItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Restrict to choices
    image = models.ImageField(upload_to='clothes/')

    def __str__(self):
        return self.name

class Outfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ClothingItem)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Outfit {self.pk} by {self.user.username}"

# Add the Profile model here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/blank-profile-picture-973460_1280.jpg')

    def save(self, *args, **kwargs):
        if not self.picture:
            self.picture = 'profile_pictures/blank-profile-picture-973460_1280.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'
