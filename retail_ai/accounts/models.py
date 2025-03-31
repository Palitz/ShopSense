from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Shopkeeper(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    shop_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'

# Customer record model (stored in 'customers' database)
class CustomerRecord(models.Model):
    customer_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    location_in_store = models.CharField(max_length=255)

    class Meta:
        app_label = 'customers'  # Ensures the database router directs this to the correct DB
