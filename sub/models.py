from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class MovieUp(models.Model):
    mname = models.CharField(max_length=30)
    mlanguage = models.CharField(max_length=30)
    mdescription = models.CharField(max_length=30)
    mpic = models.ImageField(upload_to ='img/')
    mvideo = models.FileField(upload_to ='video/')


class Price(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_days = models.IntegerField()

    def __str__(self):
        return self.name



class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Price, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"User: {self.user.username} -  Plan: {self.plan.name}"
    # expiry_date = models.DateTimeField()  # Add this field to track plan expiry

    # def __str__(self):
    #     return f"{self.user.username} - {self.plan.name}"

    # def has_active_subscription(self):
    #     return self.expiry_date > timezone.now()    

    # def calculate_remaining_days(self):
    #     current_date = timezone.now()
    #     remaining_days = (self.expiry_date - duration_in_days).days
    #     return remaining_days