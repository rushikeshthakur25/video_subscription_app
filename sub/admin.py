from django.contrib import admin
from . models import MovieUp,Price,UserSubscription

# Register your models here.
admin.site.register(MovieUp)
admin.site.register(Price)
admin.site.register(UserSubscription)