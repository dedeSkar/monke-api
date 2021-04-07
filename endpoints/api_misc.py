from utils import magic

from fastapi import APIRouter

router = APIRouter()


@router.get("/up", name="does monke-api work?")
def get_up(json: bool = False):
    return magic(response_value=True, json=json)
