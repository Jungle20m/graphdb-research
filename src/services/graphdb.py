import neo4j



class Node:
    @staticmethod
    def create_customer(driver, customer_worker_site_id):
        try:
            with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
                query = """
                        MERGE (customer:Customer {id: $customer_worker_site_id})
                        """
                result = session.run(query, customer_worker_site_id=customer_worker_site_id)
        except Exception as e:
            print(e)

    @staticmethod
    def create_voucher(driver, id, name, category_id, expiry_date, product_status, quantity, stock):
        try:
            with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
                query = """
                        MERGE (voucher:Voucher {id: $id, name: $name, category_id:$category_id, expiry_date:$expiry_date, product_status:$product_status, quantity:$quantity, stock: $stock})
                        """
                result = session.run(query,
                                    id=id,
                                    name=name,
                                    category_id=category_id,
                                    expiry_date=expiry_date,
                                    product_status=product_status,
                                    quantity=quantity,
                                    stock=stock)
        except Exception as e:
            print(e)

    @staticmethod
    def create_category(driver, id, category_code, category_name, category_status):
        try:
            with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
                query = """
                        MERGE (category:Category {id: $id, category_code: $category_code, category_name: $category_name, category_status: $category_status})
                        """
                result = session.run(query, 
                                     id=id,
                                     category_code=category_code,
                                     category_name=category_name,
                                     category_status=category_status)
        except Exception as e:
            print(e)

    @staticmethod
    def create_order(driver, id, transaction_date):
        try:
            with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
                query = """
                        MERGE (order:Order {id: $id, transation_date: $transaction_date})
                        """
                result = session.run(query, id=id, transaction_date=transaction_date)
        except Exception as e:
            print(e)


class Relationship:
    @staticmethod
    def create_customer_order(driver, customer_id, order_id):
        try:
            with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
                query = """
                        MATCH (c:Customer{id:$customer_id})
                        MATCH (o:Order{id: $order_id})
                        MERGE (c)-[:PURCHASE]->(o)
                        """
                result = session.run(query, customer_id=customer_id, order_id=order_id)
        except Exception as e:
            print(e)

    @staticmethod
    def create_order_voucher(driver, order_id, voucher_id):
        try:
            with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
                query = """
                        MATCH (v:Voucher{id:$voucher_id})
                        MATCH (o:Order{id: $order_id})
                        MERGE (o)-[:OF]->(v)
                        """
                result = session.run(query, voucher_id=voucher_id, order_id=order_id)
        except Exception as e:
            print(e)