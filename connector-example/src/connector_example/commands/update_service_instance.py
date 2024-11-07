from typing import Any

from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict


class UpdateServiceInstance(ConnectorCommand):
    def __init__(self,
        cto_id: str,
        activation_code: str,
        raise_error: bool = False,
    ):
        self.cto_id = cto_id
        self.activation_code = activation_code
        self.raise_error = raise_error

    # todo:  Make this work
    def docs(self):
        return {
            "cto_id": {"description": "The CTO ID of the service instance to update", required: True, type: "string"},
            "activation_code": {"description": "The activation code to use to update the service instance", required: True, type: "string"},
        }


    def execute(self, _config: Any, _task_data: Any) -> ConnectorProxyResponseDict:
        error: CommandErrorDict | None = None
        http_status = 200

        # uncomment this if you want to cause an exception and go down an unhappy path
        # self.raise_error = True

        if self.raise_error:
            error: CommandErrorDict = {"error_code": "401", "message": "Conflict"}
            http_status = 401

        return_response: CommandResponseDict = {
            "body": {
                "status": "success",
            },

            "mimetype": "application/json",
            "http_status": http_status,
        }

        result: ConnectorProxyResponseDict = {
            "command_response": return_response,
            "error": error,
            "command_response_version": 2,
            "spiff__logs": [],
        }

        return result
