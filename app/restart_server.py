from credential import snowflake_creds

from connector import snowflake_connector
from snowflake.core import Root

creds = snowflake_creds()

reset_server = f"""
ALTER SERVICE KING_SERVICE
  FROM SPECIFICATION $$
spec:
  containers:
    - name: {creds['app_name']}
      image: {creds['image']}:{creds['image_tag']}
      env:
       SNOWFLAKE_USER: {creds['user']}
       SNOWFLAKE_ACCOUNT: {creds['account']}
       SNOWFLAKE_WAREHOUSE: {creds['warehouse']}
       SNOWFLAKE_DATABASE: {creds['database']}
       SNOWFLAKE_PASSWORD: {creds['password']}
  endpoints:
    - name: {creds['app_name']}
      port: {creds['server_reset_port']}
      public: true  $$;
"""

snowflake_connector = snowflake_connector()
root = Root(snowflake_connector)

root.session.use_database(creds['server_reset_db'])
root.session.use_role(creds['server_reset_role'])
root.session.sql(reset_server).collect()

print("Server reset successfully")
