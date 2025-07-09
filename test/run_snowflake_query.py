import snowflake.connector
import os

print("Account value:", os.environ['SNOWFLAKE_ACCOUNT'])  # Add this

conn = snowflake.connector.connect(
    user=os.environ['SNOWFLAKE_USER'],
    password=os.environ['SNOWFLAKE_PASSWORD'],
    account='myxccrc-uja24426.us-east-1',
    warehouse='REPORTING_WAREHOUSE',
    database='ANALYTICS',
    schema='ANALYTICS_QUALITY',
    role='QC_ROLE'
)

cs = conn.cursor()
try:
    cs.execute("SELECT CURRENT_TIMESTAMP();")
    for row in cs:
        print(f"Snowflake time: {row[0]}")
finally:
    cs.close()
    conn.close()
