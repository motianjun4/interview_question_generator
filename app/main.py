from fastapi import FastAPI, Form, UploadFile, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from question import get_questions
from utils.response import ResponseType, response


import uvicorn
app = FastAPI()
@app.get("/api/question")
async def question(role:str):
    res = get_questions(role)
    # res = "1.3231, 34i23j0r"
    return response(ResponseType.SUCCESS, res)

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
uvicorn.run(app, host="0.0.0.0", port=8000)
