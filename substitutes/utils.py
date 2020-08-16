from core.models.managers.product_manager import ProductManager

def find_substitute(product_name):
    
    product = ProductManager().get_product_contains_name(product_name)

    if product:
        product_nutriscore = product.nutriscore_grade
        substitute_list = ProductManager().get_all_product_by_nutriscore_inf(product_nutriscore)
        best_substitute_list = check_intersection(substitute_list, product)
    else:
        best_substitute_list = []

    return product, best_substitute_list


def check_intersection(product_list, product):
    """This method check the instersection between two list.
        The intersection is the common element between the two list.

    Arguments:
        product_list {List} -- Contains a list of Product.
        product {Product} -- Represents the product selected by
                                        the user.

    Returns:
        [Product] -- Represents a product with a nutriscore higher than
                        the nutriscore of the selected product.
                        This product is the product with the most common
                        categories with the selected product.
    """
    best_products = []
    if len(product_list) > 0:
        
        for current_product in product_list:
            intersection_product = set(current_product.categories.all()) & set(
                    product.categories.all())

            if len(intersection_product) >= 1:
                best_products.append(current_product)
   
    return best_products