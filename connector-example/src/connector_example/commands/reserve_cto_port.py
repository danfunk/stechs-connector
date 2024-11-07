from typing import Any

from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict


class ReserveCTOPort(ConnectorCommand):
    def __init__(self,
        cto_id: str,
    ):
        self.cto_id = cto_id

    def execute(self, _config: Any, _task_data: Any) -> ConnectorProxyResponseDict:
        error: CommandErrorDict | None = None

        return_response: CommandResponseDict = {
            "body": {
                "reservation_code": "1234567890ASDFASF12341232",
                "status": "success",
                "error_description": "everything is fine"
            },


            "mimetype": "application/json",
        }

        result: ConnectorProxyResponseDict = {
            "command_response": return_response,
            "error": error,
            "command_response_version": 2,
            "spiff__logs": [],
        }

        return result
