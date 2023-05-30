from shared.exceptions import InvalidProduct
from shared.models.product import Product
from shared.repositories.base_repository import BaseRepository
from shared.repositories.product_repository import ProductRepository


class ProductManager:

    repository: BaseRepository

    def __init__(self):
        self.repository = ProductRepository()

    def get_product_by_id(self, product_id: int) -> Product:
        """
        Get product information

        :param product_id: Product identifier
        :return: Product entity
        """

        return self.repository.get_product_by_id(product_id)

    def create_product(self, product: Product) -> None:
        """
        Create a new product

        :param product: Product
        :return: None
        """

        try:
            self.repository.create_product(product)
        except InvalidProduct:
            raise
