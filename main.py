from typing import Optional
from fastapi import FastAPI
import random

monke_api = FastAPI()


@monke_api.get("/coinflip")
def get_coinflip(json: bool = False):
    coinflip = random.choice(["head", "tail"])
    if json:
        return {"data": coinflip}
    else:
        return coinflip