import  os, sys
from dotenv import dotenv_values

db_host     = os.environ.get("DB_HOST")
db_name     = os.environ.get("DB_NAME")
db_user     = os.environ.get("DB_USER")
db_password     = os.environ.get("DB_PASSWORD") 