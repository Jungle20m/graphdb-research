import csv

import neo4j
from neo4j import GraphDatabase

from src.services import files as file_service
from src.services import graphdb as graphdb_service
from src.entities.signup import ApiObject
from src.entities.signup import ApiSignupObject
from src.services.graphdb import Node, Relationship

def run():
    try:
        uri = "neo4j://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "123456"), max_connection_lifetime=1000)
        # create customer node
        with open('customer.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                Node.create_customer(driver=driver, customer_worker_site_id=row[2])
        # create voucher
        with open('voucher.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                Node.create_voucher(driver=driver, 
                                    id=row[0],
                                    name=row[1],
                                    category_id=row[2],
                                    expiry_date=row[3],
                                    product_status=row[4],
                                    quantity=row[5],
                                    stock=row[6])
        # create category
        with open('category.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                Node.create_category(driver=driver, 
                                    id=row[0],
                                    category_code=row[1],
                                    category_name=row[2],
                                    category_status=row[3])
        # create order
        with open('order.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                Node.create_order(driver=driver, id=row[0], transaction_date=row[3])
        # create relationship customer_order and order_voucher
        with open('order.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                Relationship.create_customer_order(driver=driver, customer_id=row[1], order_id=row[0])
                Relationship.create_order_voucher(driver=driver, order_id=row[0], voucher_id=row[2])
    except Exception as e:
        print(e)