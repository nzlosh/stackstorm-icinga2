from lib.icinga2 import Icinga2Action


class Icinga2RescheduleCheck(Icinga2Action):
    def run(self, object_type, filters, filter_vars=None, next_check=None, force_check=True):
        return self._client.actions.reschedule_check(
            object_type, filters, filter_vars, next_check, force_check
        )
