from lib.icinga2 import Icinga2Action


class Icinga2RemoveComment(Icinga2Action):
    def run(self, object_type, name, filters, filter_vars=None):

        return self._client.actions.remove_comment(object_type, name, filters, filter_vars=None)
