import neo4j


def create_signup(driver, **kwargs):
    print(kwargs)
    with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
        query = """
                MERGE (user:User {account_name: $account_name, date: $date, time: $time}), 
                       (ip:Ip {ip: $ip}), 
                       (dk:DeviceKey {device_key: $device_key}),
                       (user)-[:have]->(ip),
                       (user)-[:have]->(dk)
                """
        result = session.run(query,
                             account_name=kwargs["account_name"],
                             date=kwargs["date"],
                             time=kwargs["time"],
                             ip=kwargs["ip"], 
                             device_key=kwargs["device_key"])