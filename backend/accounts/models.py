from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        TUTOR = "tutor", "Tutor"

    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    email = models.EmailField(
        unique=True
    )
    role = models.CharField(
        choices=Role.choices,
        default=Role.STUDENT
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True
    )
    gender = models.CharField(
        max_length=10,
        blank=True,
        choices=Gender.choices
    )
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )