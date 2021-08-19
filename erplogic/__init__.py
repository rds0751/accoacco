# in sample_erp __init__.py
default_app_config = 'erplogic.apps.ErplogicConfig'

# in sample_erp/apps.py
from django.apps import AppConfig


class ErplogicConfig(AppConfig):
    name = 'erplogic'

    def ready(self):
        super().ready()
        from . import reports