from django.apps import AppConfig


class AModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_models'

    def ready(self):
        import a_models.signals
