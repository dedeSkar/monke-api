from utils import magic

from fastapi import APIRouter

router = APIRouter()


@router.get("/len/{string}", name="length of string")
def get_len(input: str, json: bool = False):
    _len = len(input)
    return magic(response_value=_len, json=json)