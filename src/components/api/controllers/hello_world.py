from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

hello_router = APIRouter(prefix='/hello_world')


@hello_router.get('/name/{name}')
async def hello(name: str) -> JSONResponse:
    """
    Return message

    :return: JSONResponse with message
    """

    return JSONResponse(status_code=HTTPStatus.OK, content={'message': f'Hello {name}'})
