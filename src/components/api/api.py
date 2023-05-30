from components.api.configs.configs import get_settings
from components.api.controllers.hello_world import hello_router
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette_context import plugins
from starlette_context.middleware import RawContextMiddleware

middlewares = [
    Middleware(
        RawContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        )
    )
]

app = FastAPI(title='FASTAPI - {}'.format(get_settings().APPLICATION_NAME), middleware=middlewares)

# routing
app.include_router(hello_router)
