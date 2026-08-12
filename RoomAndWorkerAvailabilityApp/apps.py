from django.apps import AppConfig


class RoomavailabilityappConfig(AppConfig):
    name = 'RoomAndWorkerAvailabilityApp'

    def ready(self):
        from . import signals