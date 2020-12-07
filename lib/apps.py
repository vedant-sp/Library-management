from django.apps import AppConfig


class LibConfig(AppConfig):
    name = 'lib'

    def ready(self):
        import lib.signals
    
