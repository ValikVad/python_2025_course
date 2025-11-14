from contextlib import AbstractContextManager

import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class TranslateReq(BaseModel):
    text: str
    source_lang: str
    target_lang: str


class Translator:
    def __init__(self):
        pass

    def translate(self, req: TranslateReq) -> str:
        return "dummy method"

    @assynccontextmanager
    async def lifespan(app: FastAPI):
        global Translator

        model_name = (
            "/Users/vadik/.cache/modelscope/hub/models/facebook/nllb-200-distilled-600M"
        )
        translator = Translator(model_name=model_name)

        yield
        del translator


app = FastAPI(lifespan=lifespan)


@app.post("/translate/")
async def translate(req: TranslateReq):
    global translator
    try:
        translated_text = translator.translate(req)
        return {"translated_text": translated_text}
    except Exception as e:
        return {"error": str(e)}
