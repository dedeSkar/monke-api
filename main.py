from fastapi import FastAPI, APIRouter

from endpoints import api_random, api_math, api_programming, api_misc, api_system
from analytics import Analytics

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
    {
        "name": "misc",
        "description": "in-dev or not assigned to a category yet ⚠️😳",
    },
]

monke_api = FastAPI(
    title="monke-api",
    description="🐵🍌 various endpoints to build your application on 🍌🦍",
    version="0.0.1",
    openapi_tags=tags_metadata
)

api_router = APIRouter()

# please keep the order as in endpoints/ for consistence 🍌
# do not forget to add a new tag!
api_router.include_router(api_math.router, tags=["math"])
api_router.include_router(api_misc.router, tags=["misc"])
api_router.include_router(api_programming.router, tags=["programming"])
api_router.include_router(api_random.router, tags=["random"])
api_router.include_router(api_system.router, tags=["sys"])


monke_api.include_router(api_router)

# initialize analytics singleton to start keeping time 🐐
analytics = Analytics()