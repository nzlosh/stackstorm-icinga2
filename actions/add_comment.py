from lib.icinga2 import Icinga2Action


class Icinga2add_comment(Icinga2Action):
    def run(self, object_type, filters, author, comment, filter_vars=None):

        return self._client.actions.add_comment(object_type, filters, author, comment, filter_vars)
