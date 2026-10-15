from django.db import models
from django.conf import settings

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(
        max_length=100,
        unique=True
    )
    subject_code = models.CharField(
        max_length=15,
        unique=True,
        blank=True
    ) 
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        if self.subject_code:
            return f'{self.subject_name} ({self.subject_code})'
        return self.subject_name
    

class TutorProfile(models.Model):
    class EducationLevel(models.TextChoices):
        PLE = "ple", "Primary Leaving Examination (PLE)"
        UCE = "uce", "Uganda Certificate of Education (UCE, O-Level)"
        UACE = "uace", "Uganda Advanced Certificate of Education (UACE, A-Level)"
        CERTIFICATE = "certificate", "Certificate"
        GRADE_III = "grade_iii", "Grade III Teaching Certificate"
        DIPLOMA = "diploma", "Diploma"
        BACHELORS = "bachelors", "Bachelor's Degree"
        PG_DIPLOMA = "pg_diploma", "Postgraduate Diploma"
        MASTERS = "masters", "Master's Degree"
        PHD = "phd", "Doctorate (PhD)"



    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_profile"
    )
    subjects = models.ManyToManyField(
        "Subject",
        related_name="tutors",
        blank=True
    )
    bio = models.TextField(
        blank=True
    )
    years_of_experience = models.PositiveSmallIntegerField(
        default=0
    )
    education_level = models.CharField(
        max_length=50,
        choices=EducationLevel.choices,
        blank=True
    )
    qualification = models.CharField(
        max_length=50,
        blank=True
    )
    institution = models.CharField(
        max_length=50,
        blank=True
    )
    hourly_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    is_verified = models.BooleanField(
        default=False 
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.get_username()