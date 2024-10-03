from os import environ, path

def snowflake_creds() -> dict:
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
            'role': environ['SNOWFLAKE_ROLE'],
            'password': environ['SNOWFLAKE_PASSWORD'],
            'warehouse': environ['SNOWFLAKE_WAREHOUSE'],
            'database': environ['SNOWFLAKE_DATABASE'],
            'server_reset_db': environ['SNOWFLAKE_RESET_SERVER_DB'],
            'server_reset_query': environ['SNOWFLAKE_RESET_SERVER_QUERY'],
            'server_reset_schema': environ['SNOWFLAKE_RESET_SERVER_SCHEMA'],
            'client_session_keep_alive': True
        }

    return creds
