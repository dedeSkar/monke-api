from fastapi import FastAPI
import random

from utils import magic

tags_metadata = [
    {
        "name": "random",
        "description": "operations based on random outcome",
    },
    {
        "name": "math",
        "description": "🐒💛🔢",
    },
    {
        "name": "programming",
        "description": "outsource your code to the monkeland 🏞️",
    },
]

monke_api = FastAPI(
    title="monke-api",
    description="🐵🍌 various endpoints to build your application on 🍌🦍",
    version="0.0.1",
    openapi_tags=tags_metadata
)


@monke_api.get("/coinflip", tags=["random"], name="siri, flip the  🪙")
def get_coinflip(json: bool = False):
    coinflip = random.choice(["head", "tail"])
    return magic(response_value=coinflip, json=json)


@monke_api.get("/8ball", tags=["random"], name="🎱")
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


@monke_api.get("/is-even/{number}", tags=["math"], name="is this number even?!")
def get_is_even(number: int, json: bool = False):
    is_even = not (number & 1 == 1)
    return magic(response_value=is_even, json=json)


@monke_api.get("/len/{string}", tags=["programming"], name="length of string")
def get_len(input: str, json: bool = False):
    _len = len(input)
    return magic(response_value=_len, json=json)
