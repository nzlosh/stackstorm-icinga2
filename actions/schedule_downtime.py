from lib.icinga2 import Icinga2Action


class Icinga2ScheduleDowntime(Icinga2Action):
    def run(
        self,
        object_type,
        filters,
        author,
        comment,
        start_time,
        end_time,
        duration,
        filter_vars=None,
        fixed=None,
        trigger_name=None,
    ):
        return self._client.actions.schedule_downtime(
            object_type,
            filters,
            author,
            comment,
            start_time,
            end_time,
            duration,
            filter_vars,
            fixed,
            trigger_name,
        )
