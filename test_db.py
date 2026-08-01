from database import execute_query

try:
    # Try fetching current PostgreSQL version
    result = execute_query("SELECT version();", fetchone=True)
    print(" Successfully connected to PostgreSQL!")
    print("DB Version:", result['version'])
except Exception as e:
    print(" Connection failed. Error details:")
    print(e)