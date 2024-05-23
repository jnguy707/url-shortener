from fastapi import FastAPI, HTTPException
import uuid
from api.requests.URLRequest import URLRequest
from models.URLModel import URLModel
import os 

# TODO: Configuration File/Decentralized Configuration
from typing import Final
host: Final[str] = "localhost"
port: Final[str] = "8000"

app = FastAPI()

@app.get("/")
async def root():
    return {"message:": "Hello World"}


'''
Future Considerations
-Index Queries
-Pagination
'''
@app.get("/list-urls")
async def get_list_urls():
    try:
        return list(URLModel.scan())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/shorten-url")
async def create_short_url(url_request: URLRequest):

    short_id = None
    if url_request.custom_short_id:
        short_id = url_request.custom_short_id
    else:
        short_id = URLModel.create_short_id()
    
    if url_request.custom_short_id:
        try:
            URLModel.get(url_request.custom_short_id)
            raise HTTPException(status_code=400, detail="Custom short ID already exists")
        except URLModel.DoesNotExist:
            pass
    
    # create entity and persist  
    url_model = URLModel(short_id=short_id, original_url=str(url_request.url))
    url_model.save()

    return {"short_url": f"http://{host}:{port}/{short_id}"}
