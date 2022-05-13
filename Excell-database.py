import pandas as pd
from sqlalchemy import create_engine
# Create a new SQLite instance in memory
engine = create_engine("sqlite://")
# Create a dummy data frame for testing or read it from Excel file using pandas.read_excel
df = pd.DataFrame({'first' : ['John', 'Sansa', 'Bran'], 'last' : ['Snow', 'Stark', 'Stark']})
# Write records stored in a DataFrame to a SQL database
df.to_sql("characters", con = engine)
# Read SQL database table into a DataFrame
pd.read_sql_table('characters', engine)