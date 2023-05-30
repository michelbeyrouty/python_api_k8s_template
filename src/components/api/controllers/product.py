from http import HTTPStatus

from components.api.managers.product_manager import ProductManager
from fastapi import APIRouter, HTTPException
from shared.exceptions import InvalidProduct
from shared.models.product import Product
from starlette.responses import JSONResponse

product_router = APIRouter(prefix='/products')
service = ProductManager()


@product_router.post('/')
async def product_create(product: Product) -> JSONResponse:
    """
    Create a product

    :param product: object containing the product_id, title and description
    :return: JSONResponse that contain the product detail
    """

    try:
        service.create_product(product)
        return product
    except InvalidProduct as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@product_router.get('/{product_id}')
async def get_product_detail(product_id: int) -> JSONResponse:
    """
    Get product detail

    :return: JSONResponse that contain the product details
    :raise: InvalidProduct
    """

    try:
        product: Product = service.get_product_by_id(product_id)
        return product
    except InvalidProduct as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))
