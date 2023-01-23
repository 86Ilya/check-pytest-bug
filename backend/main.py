from fastapi import FastAPI
from backend.views.auth import router
from backend.container import Settings, Container


def init_settings() -> Settings:
    return Settings()


def create_web_app(container=None) -> FastAPI:
    if container is None:
        container = Container()
        settings = init_settings()
        container.config.from_pydantic(settings)
    container.wire(packages=["backend"])
    container.init_resources()

    app = FastAPI()
    app.include_router(router)

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:create_web_app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        factory=True,
        log_config=None,
    )
