import pandas as pd
from sqlalchemy import create_engine


# MYSQL CONNECTION

username = ""
password = ""
host = ""
port = ""
database = "blinkitdb"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# READ CSV

file_path = r"D:\project\Blinkit_Data_Analysis-main\BlinkIT Grocery Data.csv"

df = pd.read_csv(file_path)

# CLEAN COLUMN NAMES

df.columns = df.columns.str.strip()
# REMOVE EXTRA COLUMN

if 'Sr. no' in df.columns:
    df.drop(columns=['Sr. no'], inplace=True)

# RENAME WRONG COLUMN

if 'Outlet _Identifier' in df.columns:
    df.rename(columns={
        'Outlet _Identifier': 'Outlet_Identifier'
    }, inplace=True)

# ADD MISSING COLUMN

if 'Item_Fat_Content' not in df.columns:
    df['Item_Fat_Content'] = 'Unknown'


# REORDER COLUMNS

df = df[
    [
        'Item_Fat_Content',
        'Item_Identifier',
        'Item_Type',
        'Outlet_Establishment_Year',
        'Outlet_Identifier',
        'Outlet_Location_Type',
        'Outlet_Size',
        'Outlet_Type',
        'Item_Visibility',
        'Item_Weight',
        'Sales',
        'Rating'
    ]
]

# REMOVE EMPTY ROWS

df.dropna(how='all', inplace=True)


# INSERT INTO MYSQL

df.to_sql(
    name='BLINKIT',
    con=engine,
    if_exists='append',
    index=False
)

print("Data inserted successfully!")
print("Total Rows Inserted:", len(df))
