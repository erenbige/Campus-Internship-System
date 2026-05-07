from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    
    company_name = models.CharField(max_length=255, blank=True, null=True)
    student_skills = models.TextField(blank=True, null=True, help_text="e.g., Python, Django, React")

    def __str__(self):
        return self.username