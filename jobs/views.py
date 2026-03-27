from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError 
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

from .permissions import IsStudentUser, IsCompanyOwnerOrReadOnly, IsCompanyUserOrReadOnly

class JobListView(generics.ListCreateAPIView):
    
    queryset = Job.objects.all().order_by('-created_at') 
    serializer_class = JobSerializer
    
    
    permission_classes = [IsCompanyUserOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        
        
        if not hasattr(user, 'company_profile'):
            raise ValidationError("Hata: İlan açabilmek için sistemde onaylı bir Şirket profiliniz olmalıdır.")
            
        
        serializer.save(company=user.company_profile)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsCompanyOwnerOrReadOnly]

class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser:
            return Application.objects.all().order_by('-match_score')
            
        elif getattr(user, 'is_company', False):
            return Application.objects.filter(job__company__user=user).order_by('-match_score')
            
        elif getattr(user, 'is_student', False):
            return Application.objects.filter(applicant=user).order_by('-match_score')
            
        return Application.objects.none() 

    def perform_create(self, serializer):
        user = self.request.user 
        
        if not getattr(user, 'is_student', False):
            raise PermissionDenied("Hata: Sadece öğrenci hesapları iş ilanına başvuru yapabilir!")

        job = serializer.validated_data['job']
        score = 0
        
        if user and user.is_authenticated and user.is_student:
            if job.required_skills and user.skills:
                req_skills = set(s.strip().lower() for s in job.required_skills.split(','))
                user_skills = set(s.strip().lower() for s in user.skills.split(','))
                matches = req_skills.intersection(user_skills)
                if req_skills:
                    score += (len(matches) / len(req_skills)) * 40

            if job.required_languages and user.languages:
                req_langs = set(l.strip().lower() for l in job.required_languages.split(','))
                user_langs = set(l.strip().lower() for l in user.languages.split(','))
                lang_matches = req_langs.intersection(user_langs)
                if req_langs:
                    score += (len(lang_matches) / len(req_langs)) * 30

            if job.required_experience_years > 0:
                if user.experience_years >= job.required_experience_years:
                    score += 30 
                else:
                    score += (user.experience_years / job.required_experience_years) * 30 
            else:
                score += 30 

        serializer.save(
            match_score=int(score), 
            applicant=user if (user and user.is_authenticated) else None
        )