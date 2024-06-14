import db_globals as db
from sqlalchemy import create_engine

# Database connection
engine = create_engine(db.BASE_DATABASE_URL)

# Connect to the database
connection = engine.connect()

# Define the table name from which you want to delete data
table_name = 'sensor_data'

# Construct the SQL query to delete all rows from the table
delete_query = f'DELETE FROM {table_name}'

# Execute the delete query
connection.execute(delete_query)

# Close the database connection
connection.close()
