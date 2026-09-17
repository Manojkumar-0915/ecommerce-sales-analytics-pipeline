# E-Commerce Sales & Customer Analytics Pipeline

An end-to-end Data Analytics ETL pipeline that extracts e-commerce data from live REST APIs, transforms and validates the data using Python, loads it into a MySQL Star Schema, and connects the data model to Power BI for interactive business analytics.

---

## 📌 Project Overview

This project demonstrates a complete data analytics workflow:

**Live REST APIs → Python Extraction → Data Transformation → MySQL Star Schema → Power BI → Business Insights**

The pipeline processes product, customer, and sales data from multiple API endpoints and converts the raw API data into an analytics-ready relational data model.

---

## 🏗️ Architecture

```text
                 ┌─────────────────────┐
                 │    DummyJSON APIs   │
                 │                     │
                 │  Products           │
                 │  Users              │
                 │  Carts              │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Python Extraction │
                 │      requests      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Data Transformation │
                 │      Pandas         │
                 │ Validation/Cleaning │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       MySQL        │
                 │    Star Schema     │
                 │                     │
                 │ dim_product         │
                 │ dim_customer        │
                 │ fact_sales          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Power BI      │
                 │   Data Modeling    │
                 │       DAX          │
                 │    Dashboard       │
                 └─────────────────────┘