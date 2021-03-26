from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.summary
    
class Profile(models.Model):
    profile = models.CharField(max_length=50)
    
    def __str__(self):
        return self.profile

class StudentDetails(models.Model):
    user_name = models.CharField(max_length=50)
    user_college = models.CharField(max_length=100)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)