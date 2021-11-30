from typing import Optional
import emojify
from multilang_emoji import Emoji
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.get("/emojify")
def emojize_sentence(sentence: str):
    return emojify.emojizeSentence(sentence)

# @app.get("/emojify")
# def emojize_sentence(sentence: str, lang: Optional[str] = 'hu'):
#     return emojify.emojizeSentence(sentence, Emoji(lang))
