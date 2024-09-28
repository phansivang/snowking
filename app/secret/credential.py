from os import environ, path
import snowflake.connector
from dotenv import load_dotenv
from snowflake.snowpark import Session

load_dotenv()

def connection() -> snowflake.connector.SnowflakeConnection:
    if path.isfile("/snowflake/session/token"):
        creds = {
            'host': environ['SNOWFLAKE_HOST'],
            'port': environ['SNOWFLAKE_PORT'],
            'protocol': "https",
            'account': environ['SNOWFLAKE_ACCOUNT'],
            'authenticator': "oauth",
            'token': open('/snowflake/session/token', 'r').read(),
            'warehouse': environ['SNOWFLAKE_WAREHOUSE'],
            'database': environ['SNOWFLAKE_DATABASE'],
            'schema': environ['SNOWFLAKE_SCHEMA'],
            'client_session_keep_alive': True
        }
    else:
        creds = {
            'account': environ['SNOWFLAKE_ACCOUNT'],
            'user': environ['SNOWFLAKE_USER'],
            'password': environ['SNOWFLAKE_PASSWORD'],
            'warehouse': environ['SNOWFLAKE_WAREHOUSE'],
            'database': environ['SNOWFLAKE_DATABASE'],
            'schema': environ['SNOWFLAKE_SCHEMA'],
            'client_session_keep_alive': True
        }

    return snowflake.connector.connect(**creds)

def snowflake_connector() -> Session:
    return Session.builder.configs({"connection": connection()}).create()