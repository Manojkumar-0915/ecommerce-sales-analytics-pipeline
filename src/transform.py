import pandas as pd


def transform_products(df):
    df = df.copy()

    # Keep only required product columns
    df = df[
        [
            "id",
            "title",
            "category",
            "price",
            "rating",
            "stock"
        ]
    ]

    df = df.rename(
        columns={
            "id": "product_id",
            "title": "product_name",
            "rating": "rating"
        }
    )

    return df


def transform_customers(df):
    df = df.copy()

    # Keep required customer columns
    df = df[
        [
            "id",
            "firstName",
            "lastName",
            "age",
            "gender",
            "email",
            "address"
        ]
    ]

    df["customer_name"] = (
        df["firstName"] + " " + df["lastName"]
    )

    df["city"] = df["address"].apply(
        lambda x: x["city"]
    )

    df["state"] = df["address"].apply(
        lambda x: x["state"]
    )

    df = df[
        [
            "id",
            "customer_name",
            "age",
            "gender",
            "email",
            "city",
            "state"
        ]
    ]

    df = df.rename(
        columns={
            "id": "customer_id"
        }
    )

    return df


def transform_carts(df):
    rows = []

    for _, cart in df.iterrows():

        for product in cart["products"]:

            rows.append(
                {
                    "order_id": cart["id"],
                    "customer_id": cart["userId"],
                    "product_id": product["id"],
                    "quantity": product["quantity"],
                    "unit_price": product["price"],
                    "discount_percent": product["discountPercentage"],
                    "discounted_price": product["discountedTotal"],
                    "total": product["total"]
                }
            )

    sales_df = pd.DataFrame(rows)

    return sales_df

if __name__ == "__main__":
    from extract import extract_products, extract_customers, extract_carts

    products = extract_products()
    customers = extract_customers()
    carts = extract_carts()

    products_clean = transform_products(products)
    customers_clean = transform_customers(customers)
    sales = transform_carts(carts)

    print("\nProducts:")
    print(products_clean.head())
    print("Rows:", len(products_clean))

    print("\nCustomers:")
    print(customers_clean.head())
    print("Rows:", len(customers_clean))

    print("\nSales:")
    print(sales.head())
    print("Rows:", len(sales))