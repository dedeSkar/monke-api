from utils import magic

from fastapi import APIRouter

router = APIRouter()


@router.get("/is-even/{number}", name="is this number even?!")
def get_is_even(number: int, json: bool = False):
    is_even = not (number & 1 == 1)
    return magic(response_value=is_even, json=json)

