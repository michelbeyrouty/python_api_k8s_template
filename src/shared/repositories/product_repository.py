from sqlite3 import IntegrityError

from shared.exceptions import InvalidProduct
from shared.models.product import Product
from shared.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    def get_product_by_id(self, product_id: int) -> Product:
        """
        Get product by id

        :param product_id: product identifier
        :return: Product entity
        :raise: InvalidProduct
        """
        try:
            result_id, result_title, result_desc = self.fetch_one(f'SELECT * FROM products WHERE id={product_id}')

            return Product(product_id=result_id, title=result_title, description=result_desc)
        except TypeError:
            raise InvalidProduct(f'Unable to find the product ID {product_id}')

    def create_product(self, product: Product) -> None:
        """
        Persist new product to the database

        :param product: product to save
        :return: None
        :raise: InvalidProduct
        """

        # because SQLlite is basic, check if the key already exists in the database.
        # If yes, raise an InvalidProduct exception

        try:
            result = self.get_product_by_id(product.product_id)
            if isinstance(result, Product):
                raise InvalidProduct(f'Product id # {product.product_id} already exists.')

            self.insert(
                f"INSERT INTO products VALUES ({product.product_id}, '{product.title}', '{product.description}')")
        except (InvalidProduct, InvalidProduct) as e:
            raise InvalidProduct(f'Unable to create new product. {str(e)}')

    def delete_product(self, product: Product) -> None:
        """
        Delete a product by product id
        :param product: product to delete
        :return: None
        """
        try:
            result = self.get_product_by_id(product.product_id)
            if isinstance(result, Product):
                raise InvalidProduct(f'Product id # {product.product_id} doesnt exists.')

            self.delete(f'DELETE FROM tasks WHERE id={product.product_id}')
        except (InvalidProduct, IntegrityError) as e:
            raise InvalidProduct(f'Unable to delete product. {str(e)}')
