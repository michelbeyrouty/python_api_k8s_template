from sqlite3 import OperationalError

from components.api.configs.configs import get_settings
from components.api.controllers.hello_world import hello_router
from components.api.controllers.product import product_router
from fastapi import FastAPI
from shared.repositories.base_repository import BaseRepository
from starlette.middleware import Middleware
from starlette_context import plugins
from starlette_context.middleware.raw_middleware import RawContextMiddleware

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


@app.on_event('startup')
async def startup_event() -> None:
    """
    Execute code before the application starts.
    >>>> This can be removed if not needed
    :return: None
    """
    try:
        db = BaseRepository()
        db.cur.execute('CREATE TABLE products(id primary key, title, description)')
        db.insert("""
            INSERT INTO products VALUES
                (1, 'T-shirt', 'My t-Shirt description'),
                (2, 'Short', 'My short description')
        """)
    except OperationalError as e:
        print(f'{str(e)} -- Either delete the template.db file or remove unwanted rows')

# routing
app.include_router(hello_router)
app.include_router(product_router)
