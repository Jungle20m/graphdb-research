import neo4j
from neo4j import GraphDatabase

from app.workers import main


def create_user(driver, account_name):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                CREATE (u: User {account_name: $account_name})
                RETURN id(u) AS node_id
                """
        result = session.run(query, account_name=account_name)
        record = result.single()
        return record["node_id"]


def create_ip(driver, ip):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                CREATE (i: Ip {ip: $ip})
                RETURN id(i) AS node_id
                """
        result = session.run(query, ip=ip)
        record = result.single()
        return record["node_id"]


def create_device_key(driver, device_key):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                CREATE (d: DeviceKey {device_key: $device_key})
                RETURN id(d) AS node_id
                """
        result = session.run(query, device_key=device_key)
        record = result.single()
        return record["node_id"]


def create_signup(driver, account_name, ip, device_key):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                CREATE (user:User {account_name: $account_name}), 
                       (ip:Ip {ip: $ip}), 
                       (dk:DeviceKey {device_key: $device_key}),
                       (user)-[:have]->(ip),
                       (user)-[:have]->(dk)
                """
        result = session.run(query, account_name=account_name, ip=ip, device_key=device_key)
        

if __name__ == '__main__':
    # uri = "neo4j://localhost:7687"
    # driver = GraphDatabase.driver(uri, auth=("neo4j", "123456"), max_connection_lifetime=1000)
    # # create_user(driver, account_name="0327380000")
    # # create_ip(driver, "172.16.1.137")
    # # create_device_key(driver, "e5c11a79977eca77699f4a7f30533fa7b032db054a5cf963aa7a19aaea347fc8")\
    # create_signup(driver=driver, 
    #               account_name="0327380000",
    #               ip="172.16.1.137",
    #               device_key="e5c11a79977eca77699f4a7f30533fa7b032db054a5cf963aa7a19aaea347fc8")

    main.run()