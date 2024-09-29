import logging

from snowflake.snowpark import Session
from app.configuration.credential import snowflake_creds


def snowflake_connector() -> Session:
    """Create a Snowflake session using the credentials."""
    creds = snowflake_creds()
    try:
        return Session.builder.configs(creds).create()
    except Exception as e:
        logging.error(f"Failed to connect to Snowflake: {e}")
        raise

def execute_query(query: str):
    """Execute a given query in Snowflake."""
    session = snowflake_connector()
    try:
        result = session.sql(query).collect()
        return result
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        raise
    finally:
        session.close()  # Ensure the session is closed after the query is executed
