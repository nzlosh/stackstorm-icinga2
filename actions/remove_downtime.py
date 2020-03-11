from lib.icinga2 import Icinga2Action


class Icinga2RemoveDowntime(Icinga2Action):
    def run(self, object_type, name=None, filters=None, filter_vars=None):

        return self._client.actions.remove_downtime(object_type, name, filters, filter_vars)
