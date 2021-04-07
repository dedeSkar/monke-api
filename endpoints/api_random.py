import random
from utils import magic

from fastapi import APIRouter

router = APIRouter()

@router.get("/test", name="test")
def get_test(json: bool = False):
    return magic(response_value=True, json=json)


@router.get("/coinflip", name="siri, flip the  🪙")
def get_coinflip(json: bool = False):
    coinflip = random.choice(["head", "tail"])
    return magic(response_value=coinflip, json=json)


@router.get("/8ball", name="🎱")
def get_8ball(json: bool = False):
    answer = random.choice([
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ])
    return magic(response_value=answer, json=json)