from extract import extract_products, extract_customers, extract_carts
from transform import (
    transform_products,
    transform_customers,
    transform_carts
)
from load import (
    load_products,
    load_customers,
    load_sales
)


def run_pipeline():

    print("Pipeline started...")

    # EXTRACT
    products = extract_products()
    customers = extract_customers()
    carts = extract_carts()

    print("Extract completed!")

    # TRANSFORM
    products_clean = transform_products(products)
    customers_clean = transform_customers(customers)
    sales = transform_carts(carts)

    print("Transform completed!")

    print("Products:", len(products_clean))
    print("Customers:", len(customers_clean))
    print("Sales:", len(sales))

    # LOAD
    load_products(products_clean)
    load_customers(customers_clean)
    load_sales(sales)

    print("Load completed!")
    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()