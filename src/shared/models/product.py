from pydantic.main import BaseModel


class Product(BaseModel):

    product_id: int
    title: str
    description: str
