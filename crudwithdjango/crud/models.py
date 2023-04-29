from django.db import models

# Create your models here.

# 
class User(models.Model):
    # 
    username = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # kita ingin model menampilkan username(default: User object (1))
    def __str__(self):
        return self.username

# 