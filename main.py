from typing import Union
from fastapi import FastAPI
import openai,os,json
from dotenv import load_dotenv
load_dotenv()

from openAI import routes as open_ai_route
app = FastAPI()
app.include_router(open_ai_route.router, prefix="/openai")




@app.get("/")
def read_root():
    return {"Hello": "World"}

