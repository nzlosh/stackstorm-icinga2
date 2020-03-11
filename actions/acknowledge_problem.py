from lib.icinga2 import Icinga2Action


class Icinga2AcknowledgeProblem(Icinga2Action):
    def run(
        self,
        object_type,
        filters,
        author,
        comment,
        filter_vars=None,
        expiry=None,
        sticky=None,
        notify=None,
    ):

        return self._client.actions.acknowledge_problem(
            object_type, filters, author, comment, filter_vars, expiry, sticky, notify
        )
