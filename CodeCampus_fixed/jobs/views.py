from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from .engine import MatchEngine


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_company:
            raise PermissionDenied("Only company accounts can create job listings.")
        serializer.save(company=self.request.user)


class CompanyApplicationsView(generics.ListAPIView):
    """Şirketin ilanlarına gelen tüm başvurular."""
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        if not self.request.user.is_company:
            raise PermissionDenied("Only company accounts can view applications.")
        return Application.objects.filter(job__company=self.request.user)


class StudentApplicationsView(generics.ListAPIView):
    """Öğrencinin kendi yaptığı başvurular."""
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        if not self.request.user.is_student:
            raise PermissionDenied("Only student accounts can view their applications.")
        return Application.objects.filter(applicant=self.request.user)


class ApplyForJobView(APIView):
    def post(self, request, job_id):
        user = request.user

        if not user.is_student:
            return Response({"error": "Only students can apply."}, status=status.HTTP_403_FORBIDDEN)

        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found."}, status=status.HTTP_404_NOT_FOUND)

        if Application.objects.filter(job=job, applicant=user).exists():
            return Response({"error": "You have already applied for this job."}, status=status.HTTP_400_BAD_REQUEST)

        resume_link = request.data.get('resume_link', '').strip()
        if not resume_link:
            return Response({"error": "resume_link is required."}, status=status.HTTP_400_BAD_REQUEST)

        engine = MatchEngine()
        student_skills = user.student_skills if user.student_skills else ""
        match_score = engine.calculate_score(student_skills=student_skills, job_skills=job.required_skills)

        application = Application.objects.create(
            job=job,
            applicant=user,
            resume_link=resume_link,
            match_score=match_score
        )

        return Response(
            {"message": "Successfully applied!", "job": job.title, "match_score": application.match_score},
            status=status.HTTP_201_CREATED
        )


class ApplicationStatusUpdateView(APIView):
    """Şirketin başvuru durumunu güncellemesi için."""
    def patch(self, request, app_id):
        if not request.user.is_company:
            return Response({"error": "Only companies can update application status."}, status=status.HTTP_403_FORBIDDEN)

        try:
            application = Application.objects.get(id=app_id, job__company=request.user)
        except Application.DoesNotExist:
            return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get('status')
        valid_statuses = [s[0] for s in Application.STATUS_CHOICES]
        if new_status not in valid_statuses:
            return Response({"error": f"Invalid status. Choose from: {valid_statuses}"}, status=status.HTTP_400_BAD_REQUEST)

        application.status = new_status
        application.save()

        return Response({"message": "Status updated.", "status": application.status})
