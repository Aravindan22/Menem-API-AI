from typing import Union,Annotated
from fastapi import APIRouter, File, UploadFile
import openai,os,json


from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
router = APIRouter()


@router.get("/text-completion")
def get_text_completion(text: str, type:str = ""):
    
    # https://platform.openai.com/docs/api-reference/completions/create?lang=python
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.4,
        max_tokens= 50 if type == "caption" else 4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    
    completion= response.choices[0].text.strip().strip('"')
    return completion


@router.get("/image-creation")
def generate_image(text: str):
    # https://platform.openai.com/docs/api-reference/completions/create?lang=python
    response = openai.Image.create(
                prompt=text,
                n=1,
                size="1024x1024"
                )
    return response.data[0]


@router.post("/image-edit")
def edit_image(text: str, file: Annotated[bytes, File()] ):
    openai.Image.create_edit(
    image=open(file, "rb"),
    prompt=text,
    n=2,
    size="1024x1024"
    )

