from app.configuration.credential import snowflake_creds

from app.connection.connector import snowflake_connector
from snowflake.core import Root

creds = snowflake_creds()

root = Root(snowflake_connector())
root.session.use_role(creds['role']) # select role
root.session.use_database(creds['server_reset_db']) # select database
root.session.use_schema(creds['server_reset_schema']) # select schema
# select database and schema where is your procedure being stored.

root.session.sql('CALL RESTART_SERVER_DEV();').collect() # call procedure function
print("Server reset successfully")

