import neo4j
from neo4j import GraphDatabase

from src.services import files as file_service
from src.services import graphdb as graphdb_service
from src.entities.signup import ApiObject
from src.entities.signup import ApiSignupObject


def run():
    try:
        uri = "neo4j://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "123456"), max_connection_lifetime=1000)
        # some comment
        rows = file_service.read_lines(file_location="src/resources/api.txt")
        for row in rows:
            api_object = ApiObject.get_from_row_of_log(row=row)
            if not api_object.is_signup_new_account():
                continue
            api_signup_object = ApiSignupObject.get_from_api_json_log(api_json_log=api_object.json_log)
            graphdb_service.create_signup(driver=driver,
                                          account_name=api_signup_object.account_name,
                                          date=api_object.date_,
                                          time=api_object.time_,
                                          ip=api_object.ip,
                                          device_key=api_signup_object.device_key)
    except Exception as e:
        print(e)