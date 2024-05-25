from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.connection.base import Connection
import os
import uuid
import random
from dotenv import load_dotenv

# TODO: Decentralized Credentials
load_dotenv()

class URLModel(Model):
    class Meta:
        table_name = "url_mapping"
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        host = os.getenv('DYNAMODB_ENDPOINT_URL')
        region = os.getenv("AWS_REGION")
    
    short_id = UnicodeAttribute(hash_key=True)
    original_url = UnicodeAttribute()

    def create_short_id() -> str:
        rand_length = random.randint(4,12)
        return str(uuid.uuid4())[:rand_length]
    
# Table Check
if not URLModel.exists():
    URLModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
