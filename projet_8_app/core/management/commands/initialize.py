from core.models.product import Product
from core.models.managers.openfoodfact_manager import OffManager
from core.models.managers.product_manager import ProductManager
from core.models.managers.category_manager import CategoryManager

def initialize_job():
    """This function is the job to create tables in db and populates db with
    products from the openfoodfacts base.
    """
    openfoodfact_manager = OffManager()
    openfoodfact_manager.download_product()

    product_list = openfoodfact_manager.data
    ProductManager().insert_product_db(product_list)
    
    