from rest_framework import serializers
from .models import Job, Application


class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name', read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'company_name', 'title', 'description', 'required_skills', 'created_at']
        read_only_fields = ['id', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(source='applicant.username', read_only=True)
    job_title = serializers.CharField(source='job.title', read_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'job_title', 'applicant_name',
            'resume_link', 'status', 'match_score', 'applied_at'
        ]
        read_only_fields = ['id', 'match_score', 'applied_at', 'status']
