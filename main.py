from fastapi import FastAPI, APIRouter

from endpoints import api_random, api_math, api_programming

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

api_router = APIRouter()
api_router.include_router(api_random.router, tags=["random"])
api_router.include_router(api_math.router, tags=["math"])
api_router.include_router(api_programming.router, tags=["programming"])

monke_api.include_router(api_router)
