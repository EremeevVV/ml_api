from fastapi import FastAPI

from ml_api.router import route as ml_route


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(ml_route)
    return app
