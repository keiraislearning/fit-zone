from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid

class Fit(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]

    name = models.CharField(max_length=255)  
    price = models.IntegerField(default=0)  
    description = models.TextField()  
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    views = models.IntegerField(default=0) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_fit_hot(self):
        return self.views > 20
        
    def increment_views(self):
        self.views += 1
        self.save()