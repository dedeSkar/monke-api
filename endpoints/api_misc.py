from utils import magic

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/ip", name="your ip address")
def get_ip(request: Request, json: bool = False):
    return magic(response_value=request.client.host, json=json)


@router.get("/headers", name="your request headers")
def get_ip(request: Request):
    return request.headers
