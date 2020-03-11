from lib.icinga2 import Icinga2Action


class Icinga2SendCustomNotification(Icinga2Action):
    def run(self, object_type, filters, author, comment, filter_vars=None, force=False):
        return self._client.actions.send_custom_notification(
            object_type, filters, author, comment, filter_vars, force
        )
