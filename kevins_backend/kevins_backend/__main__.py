import os

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles


def create_app():
    app = fastapi.FastAPI()

    # mount the build javascript files in production build, otherwise run locally with webpack
    if not bool(os.getenv("LOCAL_WEBPACK")):
        app.mount("/", StaticFiles(directory="/app/static", html=True), name="/")

    return app


if __name__ == "__main__":
    config = uvicorn.Config(create_app(), host="0.0.0.0", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
