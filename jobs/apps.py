from django.apps import AppConfig
from django.apps import AppConfig


class JobsConfig(AppConfig):
    name = 'jobs'

class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobs'

    
    def ready(self):
        import jobs.signals
