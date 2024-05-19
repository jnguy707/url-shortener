from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import uuid
import random

class URLModel(Model):
    class Meta:
        table_name = "urls"
        region = "TBD"
    
    short_id = UnicodeAttribute(hash_key=True)
    original_url = UnicodeAttribute()

    def create_short_id() -> str:
        rand_length = random.randint(4,12)
        return str(uuid.uuid4()[:rand_length])

# Table Check
if not URLModel.exists():
    URLModel.create_table(wait=True)