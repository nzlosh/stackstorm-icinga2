from lib.icinga2 import Icinga2Action


class Icinga2DelayNotification(Icinga2Action):
    def run(self, object_type, filters, timestamp, filter_vars=None):
        return self._client.actions.delay_notification(object_type, filters, timestamp, filter_vars)
