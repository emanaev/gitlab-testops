from typing import Union
from fastapi import FastAPI
import gitlab
import time
import os
import logging
logger = logging.getLogger(__name__)


GITLAB_URL='http://gitlab'
GITLAB_TOKEN=os.environ['GITLAB_TOKEN']


gl = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_TOKEN)
logger.info(f"Waiting for GITLAB [{GITLAB_URL}] ...")
while True:
    try:
        gl.auth()
        break
    except:
        time.sleep(3)  
logger.info("GITLAB is up!")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
