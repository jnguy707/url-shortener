from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import uuid

class URLModel(Model):
    class Meta:
        table_name = "urls"
        region = "TBD"
    
    short_id = UnicodeAttribute(hash_key=True)
    original_url = UnicodeAttribute()

if not URLModel.exists():
    URLModel.create_table(wait=True)