import snowflake.connector
import os

conn = snowflake.connector.connect(
    user=os.environ['SNOWFLAKE_USER'],
    password=os.environ['SNOWFLAKE_PASSWORD'],
    account=os.environ['SNOWFLAKE_ACCOUNT'],
    warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
    database=os.environ['SNOWFLAKE_DATABASE'],
    schema=os.environ['SNOWFLAKE_SCHEMA'],
    role=os.environ['SNOWFLAKE_ROLE']
)

cs = conn.cursor()
try:
    cs.execute("SELECT CURRENT_TIMESTAMP();")
    for row in cs:
        print(f"Snowflake time: {row[0]}")
finally:
    cs.close()
    conn.close()
