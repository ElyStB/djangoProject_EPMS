from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoProject_EPMS.accounts'

    def ready(self):
        import djangoProject_EPMS.accounts.signals
