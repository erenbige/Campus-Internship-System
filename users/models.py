from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False, verbose_name="Student Account")
    is_company = models.BooleanField(default=False, verbose_name="Company Account")
    
    
    skills = models.CharField(
        max_length=500, 
        blank=True, 
        null=True, 
        verbose_name="Technical Skills",
        help_text="Comma separated. Example: Python, Django, React"
    )
    languages = models.CharField(
        max_length=500, 
        blank=True, 
        null=True, 
        verbose_name="Spoken Languages",
        help_text="Comma separated. Example: English, German"
    )
    experience_years = models.PositiveIntegerField(
        default=0, 
        verbose_name="Years of Experience",
        help_text="Example: 1, 2, or 0 for fresh graduates"
    )

    def __str__(self):
        return self.username