from django.apps import AppConfig


class ThmrApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'thmr_api'

    def ready(self):
        import thmr_api.signals 
