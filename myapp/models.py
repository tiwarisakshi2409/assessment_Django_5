from django.db import models
from django.utils import timezone


# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    flatno=models.PositiveBigIntegerField(default=100)
    members=models.PositiveBigIntegerField(default=100)
    mobile=models.PositiveIntegerField()
    password=models.CharField(max_length=50)
    def __str__(self):
            return self.name
    
class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
            return self.email
        
# models.py

class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    occupation = models.CharField(max_length=255)

    government_id = models.ImageField(upload_to='government_ids/', null=True, blank=True)
    photo = models.ImageField(upload_to='member_photos/', null=True, blank=True)
    proof_of_residence = models.ImageField(upload_to='proof_of_residence/', null=True, blank=True)

    def __str__(self):
        return self.full_name

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=timezone.now())
    

class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())


