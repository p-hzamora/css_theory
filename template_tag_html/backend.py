from dotenv import load_dotenv
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from extension.orm.orm.condition_types import ConditionType
from template_tag_html.models.address import AddressModel, AddressValidator
from extension.orm import MySQLRepository

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
db = MySQLRepository(USER, PASSWORD, "sakila").connect()

address_model = AddressModel(db)

regex = r"^(A|B|C)"
addresses, cities = address_model.where(
    lambda a: (a.City.city, ConditionType.REGEXP, regex), regex=regex
).select(lambda a: (a, a.City))


for address in addresses:
    validator = AddressValidator()
    validate = validator.validate(address)
    if not validate.is_valid:
        for err in validate.errors:
            print(err.ErrorMessage)
print("Listado correcto")
