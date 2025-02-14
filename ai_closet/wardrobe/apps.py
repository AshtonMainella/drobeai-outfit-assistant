from django.apps import AppConfig

class WardrobeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wardrobe'

    def ready(self):
        import wardrobe.signals  # Import signals here
