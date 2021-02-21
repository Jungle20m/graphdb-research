import neo4j
from neo4j import GraphDatabase


def create_signup(driver, **kwargs):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                MERGE (user:User {account_name: $account_name, date: $date, time: $time}) 
                MERGE (ip:Ip {ip: $ip})
                MERGE (dk:DeviceKey {device_key: $device_key})
                MERGE      (user)-[:have]->(ip),
                      (user)-[:have]->(dk)
                """
        result = session.run(query,
                             account_name=kwargs["account_name"],
                             date=kwargs["date"],
                             time=kwargs["time"],
                             ip=kwargs["ip"], 
                             device_key=kwargs["device_key"])


def create_node(driver, account_name, date, time, ip, device_key):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                MERGE (user:User {account_name: $account_name, date: $date, time: $time})
                MERGE (ip:IP {ip: $ip})
                MERGE (dk:DeviceKey {device_key: $device_key})
                """
        result = session.run(query, account_name=account_name, date=date, time=time, ip=ip, device_key=device_key)


def create_user_to_ip_relationship(driver, account_name, date, time, ip):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                MATCH (user:User {account_name: $account_name, date: $date, time: $time})
                MATCH (ip:IP {ip: $ip})
                MERGE (user)-[:HAVE]->(ip)
                """
        result = session.run(query, account_name=account_name, date=date, time=time, ip=ip)


def create_user_to_devicekey_relationship(driver, account_name, date, time, device_key):
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                MATCH (user:User {account_name: $account_name, date: $date, time: $time})
                MATCH (dk:DeviceKey {device_key: $device_key})
                MERGE (user)-[:HAVE]->(dk)
                """
        result = session.run(query, account_name=account_name, date=date, time=time, device_key=device_key)


def run():
    try:
        uri = "neo4j://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "123456"), max_connection_lifetime=1000)
        # some comment
        create_node(driver=driver, account_name="0327380002", date="2021-01-23", time="15:30:20", ip="1.53.252.177", device_key="xxxyyzzzt")
        create_user_to_ip_relationship(driver=driver, account_name="0327380002", date="2021-01-23", time="15:30:20", ip="1.53.252.177")
        create_user_to_devicekey_relationship(driver=driver, account_name="0327380002", date="2021-01-23", time="15:30:20", device_key="xxxyyzzzt")
    except Exception as e:
        print(e)