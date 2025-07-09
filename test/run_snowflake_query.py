import snowflake.connector
import os

conn = snowflake.connector.connect(
    user=os.environ['NATE_NORTON'],
    password=os.environ['Twinkie6369639!'],
    account=os.environ['MYXCCRC-UJA24426.snowflakecomputing.com'],
    warehouse=os.environ['REPORTING_WAREHOUSE'],
    database=os.environ['ANALYTICS'],
    schema=os.environ['ANALYTICS_QUALITY'],
    role=os.environ['QC_ROLE']
)

cs = conn.cursor()
try:
    cs.execute("SELECT CURRENT_TIMESTAMP();")
    for row in cs:
        print(f"Snowflake time: {row[0]}")
finally:
    cs.close()
    conn.close()
