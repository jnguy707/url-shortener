from fastapi import FastAPI, HTTPException
from requests.URLRequest import URLRequest
from models.URLModel import URLModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message:": "Hello World"}

'''
Considerations
-Index Queries
-Pagination
'''
@app.get("/list-urls")
async def get_list_urls():
    try:
        return list(URLModel.scan())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    