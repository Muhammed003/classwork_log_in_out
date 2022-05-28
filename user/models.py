from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, username=None, email=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, email=None, username=None, **extra_fields)

    def create_superuser(self, phone_number, email=None, username=None, password=None, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password,  email=None, username=None, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=150)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ["username", ]

    objects = CustomUserManager()

    @staticmethod
    def generate_activation_code(length: int, number_range: str):
        from django.utils.crypto import get_random_string
        return get_random_string(length, number_range)

    def save(self, *args, **kwargs):
        self_activation_code = self.generate_activation_code(10, "qwerty123456789")
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.phone_number)


