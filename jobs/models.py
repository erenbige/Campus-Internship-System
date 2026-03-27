from django.db import models
from django.conf import settings 

class Company(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company_profile', null=True, blank=True)
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True) 
    industry = models.CharField(max_length=50, blank=True, null=True) 

    class Meta:
        verbose_name_plural = "Companies"
        
    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
   
    required_skills = models.CharField(
        max_length=500, blank=True, null=True, 
        help_text="Comma separated. Example: Python, React, SQL"
    )
    required_languages = models.CharField(
        max_length=500, blank=True, null=True, 
        help_text="Comma separated. Example: English, German"
    )
    required_experience_years = models.PositiveIntegerField(
        default=0, 
        help_text="Minimum years of experience required"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    match_score = models.IntegerField(default=0, verbose_name="ATS Match Score (%)")
    
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    resume_link = models.URLField(blank=True, null=True)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} -> {self.job.title} (Score: %{self.match_score})"