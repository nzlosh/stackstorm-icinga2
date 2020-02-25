from lib.icinga2 import Icinga2Action


class Icinga2ProcessCheckResult(Icinga2Action):
    """
        Return example:
        process_check_result('Service',
                             'myhost.domain!ping4',
                             'exit_status': 2,
                             'plugin_output': 'PING CRITICAL - Packet loss = 100%',
                             'performance_data': [
                                 'rta=5000.000000ms;3000.000000;5000.000000;0.000000',
                                 'pl=100%;80;100;0'],
                             'check_source': 'python client'})
     """

    def run(
        self,
        object_type="",
        name="",
        exit_status="",
        plugin_output="",
        check_command=[],
        check_source="",
    ):
        return self._client.actions.process_check_result(
            object_type,
            name,
            exit_status,
            plugin_output,
            check_command=check_command,
            check_source=check_source,
        )
