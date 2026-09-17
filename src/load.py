import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="ecommerce_db"
    )

    return connection


def load_products(df):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO dim_product
    (product_id, product_name, category, price, rating, stock)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        product_name = VALUES(product_name),
        category = VALUES(category),
        price = VALUES(price),
        rating = VALUES(rating),
        stock = VALUES(stock)
    """

    for _, row in df.iterrows():
        values = (
            row["product_id"],
            row["product_name"],
            row["category"],
            row["price"],
            row["rating"],
            row["stock"]
        )

        cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    print("Products loaded successfully!")


def load_customers(df):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO dim_customer
    (customer_id, customer_name, age, gender, email, city, state)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        customer_name = VALUES(customer_name),
        age = VALUES(age),
        gender = VALUES(gender),
        email = VALUES(email),
        city = VALUES(city),
        state = VALUES(state)
    """

    for _, row in df.iterrows():
        values = (
            row["customer_id"],
            row["customer_name"],
            row["age"],
            row["gender"],
            row["email"],
            row["city"],
            row["state"]
        )

        cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    print("Customers loaded successfully!")


def load_sales(df):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO fact_sales
    (order_id, customer_id, product_id, quantity,
     unit_price, discount_percent, discounted_price, total)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        values = (
            row["order_id"],
            row["customer_id"],
            row["product_id"],
            row["quantity"],
            row["unit_price"],
            row["discount_percent"],
            row["discounted_price"],
            row["total"]
        )

        cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    print("Sales loaded successfully!")