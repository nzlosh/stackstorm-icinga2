from lib.icinga2 import Icinga2Action


class Icinga2RemoveAcknowledgement(Icinga2Action):
    def run(self, object_type, filters, filter_vars=None):
        return self._client.actions.remove_acknowledgement(object_type, filters, filter_vars)
