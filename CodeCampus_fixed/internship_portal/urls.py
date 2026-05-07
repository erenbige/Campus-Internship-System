from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='login.html')),

    path(
        'student-dashboard/',
        TemplateView.as_view(
            template_name='student-dashboard.html'
        )
    ),

    path(
        'company-dashboard/',
        TemplateView.as_view(
            template_name='company-dashboard.html'
        )
    ),

    path('api/users/', include('users.urls')),
    path('api/jobs/', include('jobs.urls')),
]