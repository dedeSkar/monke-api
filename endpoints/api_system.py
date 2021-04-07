from fastapi import APIRouter

from utils import magic
from analytics import Analytics


router = APIRouter()


@router.get("/up", name="does monke-api work?")
def get_up(json: bool = False):
    return magic(response_value=True, json=json)


@router.get("/uptime", name="how long is monke-api up in seconds?")
def get_uptime(json: bool = False):
    a = Analytics()
    return magic(response_value=a.get_uptime(), json=json)
