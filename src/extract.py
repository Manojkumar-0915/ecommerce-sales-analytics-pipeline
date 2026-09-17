import requests
import pandas as pd


def extract_products():
    url = "https://dummyjson.com/products?limit=0"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["products"])

    return df


def extract_customers():
    url = "https://dummyjson.com/users?limit=0"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["users"])

    return df


def extract_carts():
    url = "https://dummyjson.com/carts?limit=0"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["carts"])

    return df


if __name__ == "__main__":

    products = extract_products()
    customers = extract_customers()
    carts = extract_carts()

    print("Products extracted:", len(products))
    print("Customers extracted:", len(customers))
    print("Carts extracted:", len(carts))

    print("\nCart sample:")
    print(carts.head())