from utils import magic

from fastapi import APIRouter

router = APIRouter()


@router.get("/is-even/{number}", name="is this number even?!")
def get_is_even(number: int, json: bool = False):
    is_even = not (number & 1 == 1)
    return magic(response_value=is_even, json=json)

@router.get("/is_prime/{number}", name="is this number based? or nonprimelet")
def is_number_prime(number :int, json :bool = False):
    div_count = 0
    if number == 2:
        return True
    elif number == 1:
        return False
    else:
        for i in range(1, (round(math.sqrt(number))+1)):
            if number % i == 0: 
                div_count += 1
            if div_count > 1: 
                break
        if div_count == 1:
            is_prime = True
        else: 
            is_prime = False
    return magic(response_value=is_prime, json=json)
