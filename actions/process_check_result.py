from lib.icinga2 import Icinga2Action


class Icinga2ProcessCheckResult(Icinga2Action):
    def run(
        self,
        object_type,
        name,
        exit_status,
        plugin_output,
        performance_data=None,
        check_command=None,
        check_source=None,
    ):
        return self._client.actions.process_check_result(
            object_type,
            name,
            exit_status,
            plugin_output,
            performance_data,
            check_command,
            check_source,
        )
