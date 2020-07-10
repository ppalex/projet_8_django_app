from core.models.product import Product
from core.managers.openfoodfact_manager import OffManager

def initialize_job():
    """This function is the job to create tables in db and populates db with
    products from the openfoodfacts base.
    """
    openfoodfact_manager = OffManager()
    openfoodfact_manager.download_product()

    import pdb; pdb.set_trace()