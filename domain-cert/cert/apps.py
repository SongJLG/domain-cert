from django.apps import AppConfig


class CertConfig(AppConfig):
    name = 'cert'

    def ready(self):
        import cert.api.signals_handler
        import cert.views
        super(CertConfig, self).ready()