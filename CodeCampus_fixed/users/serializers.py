from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(
        choices=['student', 'company'],
        write_only=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'username', 'password', 'email',
            'user_type', 'company_name', 'student_skills'
        ]

    def validate(self, data):
        user_type = data.get('user_type')
        if user_type == 'company' and not data.get('company_name', ''):
            raise serializers.ValidationError(
                {"company_name": "company_name is required for company accounts."}
            )
        if user_type == 'student' and not data.get('student_skills', ''):
            raise serializers.ValidationError(
                {"student_skills": "student_skills is required for student accounts."}
            )
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_student', 'is_company', 'company_name', 'student_skills']
