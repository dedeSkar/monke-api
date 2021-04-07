from utils import magic

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/ip", name="your ip address")
def get_ip(request: Request, json: bool = False):
    return magic(response_value=request.client.host, json=json)


@router.get("/headers", name="your request headers")
def get_ip(request: Request):
    return request.headers


@router.get("/lorem-ipsum/{length}", name="lorem ipsum generator")
def get_lorem_ipsum(length: int, json: bool = False):

    def _split_custom(word):
        return [char for char in word]
    
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce risus mi, blandit a purus a, vulputate 
    dignissim orci. Fusce ut tortor mi. Duis finibus tristique libero, sit amet vestibulum est ornare vitae. Quisque 
    in tellus id velit vehicula varius. Quisque non maximus nibh, a auctor turpis. Etiam mattis lacinia nulla, 
    porta pulvinar sapien varius vitae. Pellentesque sit amet volutpat ligula, id commodo ante. """
    text = text.split(' ')[:length]
    separator = " "
    last = _split_custom(text[len(text)-1])
    length = len(last)

    if last[length - 1] == "," or last[length - 1] == ".":
        last[length-1] = ""

    lastword = ""
    lastword = lastword.join(last)
    text[len(text)-1] = lastword

    return magic(response_value=separator.join(text), json=json)
