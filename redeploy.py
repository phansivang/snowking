from app.configuration.credential import snowflake_creds

from app.connection.connector import snowflake_connector
from snowflake.core import Root

creds = snowflake_creds()
connector = snowflake_connector()

root = Root(snowflake_connector())
root.session.use_database(creds['server_reset_db']) # select database
root.session.use_role(creds['role']) # select role

result = root.session.sql(creds['server_reset_query']).collect() # call procedure function
print("Server reset successfully")

