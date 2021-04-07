from typing import Any


def magic(response_value: Any, json: bool = False):
    return {"data": response_value} if json else response_value
