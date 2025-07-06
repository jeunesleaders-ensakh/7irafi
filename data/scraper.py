import csv
import os.path

from data.functionalities import get_products_shopify_store_all_pages

# Configurations
DATA_FOLDER = 'data'
os.makedirs(DATA_FOLDER, exist_ok=True)  # Ensure the data folder is existing

# 1. Scraping data from Shopify stores
STORES = [
    {"csv_filename": "artisans_du_maroc.csv", "base_url": "https://artisans-dumaroc.com/"},
    {"csv_filename": "chabi_chic.csv", "base_url": "https://www.chabi-chic.com/"},
    {"csv_filename": "mytindy.csv", "base_url": "https://mytindy.com/"}
]

for store in STORES:
    store_products = get_products_shopify_store_all_pages(store["base_url"], 250)

    with open(os.path.join(DATA_FOLDER, store["csv_filename"]), 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=store_products[0].keys())
        writer.writeheader()
        writer.writerows(store_products)
