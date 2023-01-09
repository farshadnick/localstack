from typing import Final

from jsonpath_ng import parse

from localstack.services.stepfunctions.asl.component.state.state_wait.wait_function.seconds import (
    Seconds,
)
from localstack.services.stepfunctions.asl.component.state.state_wait.wait_function.wait_function import (
    WaitFunction,
)
from localstack.services.stepfunctions.asl.eval.environment import Environment


class SecondsPath(WaitFunction):
    # SecondsPath
    # A time, in seconds, to state_wait before beginning the state specified in the Next
    # field, specified using a path from the state's input data.
    # You must specify an integer value for this field.

    def __init__(self, path: str):
        self.path: Final[str] = path

    def _eval_body(self, env: Environment) -> None:
        input_expr = parse(self.path)
        seconds = input_expr.find(env.inp)
        seconds_func = Seconds(seconds)
        seconds_func.eval(env)
