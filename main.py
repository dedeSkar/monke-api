from fastapi import FastAPI
import random

from utils import magic

monke_api = FastAPI()


@monke_api.get("/coinflip")
def get_coinflip(json: bool = False):
    coinflip = random.choice(["head", "tail"])
    return magic(response_value=coinflip, json=json)


@monke_api.get("/is-even/{number}")
def get_is_even(number: int, json: bool = False):
    is_even = not (number & 1 == 1)
    return magic(response_value=is_even, json=json)
