from django.apps import AppConfig


class ErplogicConfig(AppConfig):
    name = 'erplogic'

    def ready(self):
        super().ready()
        from . import reports
