import pandas as pd
from sqlalchemy import create_engine

# =========================
# MYSQL CONNECTION
# =========================

username = ""
password = ""
host = ""
port = ""
database = "blinkitdb"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# =========================
# READ CSV
# =========================

file_path = r"D:\project\Blinkit_Data_Analysis-main\BlinkIT Grocery Data.csv"

df = pd.read_csv(file_path)

# =========================
# CLEAN COLUMN NAMES
# =========================

df.columns = df.columns.str.strip()
