from typing import Union
from fastapi import APIRouter
import openai,os,json


from dotenv import load_dotenv
load_dotenv()

router = APIRouter()


@router.get("/text-completion")
def get_text_completion(text: str):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    # https://platform.openai.com/docs/api-reference/completions/create?lang=python
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.4,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    
    completion= response.choices[0].text.strip().strip('"')
    return completion


@router.get("/image-creation")
def generate_image(text: str):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    # https://platform.openai.com/docs/api-reference/completions/create?lang=python
    response = openai.Image.create(
                prompt=text,
                n=1,
                size="1024x1024"
                )
    return response.data[0]