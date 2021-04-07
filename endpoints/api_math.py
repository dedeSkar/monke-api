from utils import magic

from fastapi import APIRouter

router = APIRouter()


@router.get("/is-even/{number}", name="is this number even?!")
def get_is_even(number: int, json: bool = False):
    is_even = not (number & 1 == 1)
    return magic(response_value=is_even, json=json)


@router.get("/how_many_bananas_there_are_in/", name="how many bananas there are in X distance(c,m,km)")
def banana_in_m_counter(number : int, distance : str, json: bool = False ):
    if distance == 'm':
        return magic(response_value=int(round(number/0.2021)), json=json)
    elif distance == 'cm':
        return magic(response_value=int(round(number/20.32)), json=json)
    elif distance == 'km':
        return magic(response_value=int(round(number/0.0002032)), json=json)

