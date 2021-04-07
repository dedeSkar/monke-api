import random, string, json
from utils import magic

from fastapi import APIRouter

router = APIRouter()


@router.get("/coinflip", name="siri, flip the  🪙")
def get_coinflip(json: bool = False):
    answer = random.choice(["head", "tail"])
    return magic(response_value=answer, json=json)


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


@router.get("/random-password/", name="monke wants security")
def password_gen(length : int, include_sym : bool, json: bool = False):
    gen_password = ''
    similar_letters_list = ['i', 'I', 'L', 'l', 'O', 'o']

    for i in range(0, length):
        gen_password += random.choice(string.ascii_letters)

        while True:
            if gen_password[i] in similar_letters_list:
                gen_password = gen_password[:-1]
                gen_password += random.choice(string.ascii_letters)
            else:
                break

        if random.randint(0,100) > 70:
            gen_pass_list= list(gen_password)
            gen_pass_list[i] = str(random.choice(string.digits))
            gen_password = "".join(gen_pass_list)

        if random.randint(0,100) > 80 and include_sym == True:
            gen_pass_list= list(gen_password)
            gen_pass_list[i] = str(random.choice(string.punctuation))
            gen_password = "".join(gen_pass_list)   

    return magic(response_value=gen_password, json=json)
