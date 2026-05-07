from django.urls import path
from .views import (
    JobListCreateView,
    ApplyForJobView,
    CompanyApplicationsView,
    StudentApplicationsView,
    ApplicationStatusUpdateView,
)

urlpatterns = [
    path('', JobListCreateView.as_view(), name='job_list_create'),
    path('<int:job_id>/apply/', ApplyForJobView.as_view(), name='apply_for_job'),
    path('applications/', CompanyApplicationsView.as_view(), name='company_applications'),
    path('my-applications/', StudentApplicationsView.as_view(), name='student_applications'),
    path('applications/<int:app_id>/status/', ApplicationStatusUpdateView.as_view(), name='application_status_update'),
]
