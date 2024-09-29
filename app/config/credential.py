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
            'password': environ['SNOWFLAKE_PASSWORD'],
            'warehouse': environ['SNOWFLAKE_WAREHOUSE'],
            'database': environ['SNOWFLAKE_DATABASE'],
            'app_name': environ['SNOWFLAKE_APP_NAME'],
            'image': environ['SNOWFLAKE_IMAGE'],
            'server_reset_db': environ['SNOWFLAKE_RESET_SERVER_DB'],
            'server_reset_role': environ['SNOWFLAKE_RESET_SERVER_ROLE'],
            'server_reset_port': environ['SNOWFLAKE_PORT'],
            'image_tag': environ['IMAGE_TAG'],
            'client_session_keep_alive': True
        }

    return creds
