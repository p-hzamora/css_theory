from .orm import MySQLRepository
from decouple import config

USERNAME = config("USERNAME")
PASSWORD = config("PASSWORD")
DATABASE = config("DATABASE")
db = MySQLRepository(user=USERNAME, password=PASSWORD, database=DATABASE)
