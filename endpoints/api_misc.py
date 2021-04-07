from utils import magic

from fastapi import APIRouter

router = APIRouter()


@router.get("/up", name="does monke-api work?")
def get_up(json: bool = False):
    return magic(response_value=True, json=json)

@router.get("/should_you_live_in_lithuania")
def should_you_live_in_lithuania(json: bool = False):
    #todo update to True, when the situation changes
    return magic(response_value-False, json=json)
