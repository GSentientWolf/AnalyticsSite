from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "analytics_site.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import analytics_site.users.signals  # noqa: F401
        except ImportError:
            pass
