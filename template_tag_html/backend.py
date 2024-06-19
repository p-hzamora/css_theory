from dotenv import load_dotenv
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from extension.orm.orm.condition_types import ConditionType
from template_tag_html.models import AddressModel
from extension.orm import MySQLRepository

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
db = MySQLRepository(USER, PASSWORD, "sakila").connect()

address_model = AddressModel(db)

regex = r"^(A|B|C)"
responsive = address_model.where(
    lambda a: (a.City.city, ConditionType.REGEXP, regex), regex=regex
).select(lambda a: (a, a.City.Country))


for a in responsive:
    a
