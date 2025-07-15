# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import  HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import api
import os 
import chatbot
from scraper import web_scrape 
from dotenv import load_dotenv
from init import init_db
load_dotenv() # Load environment variables
init_db()  # Initialize the database    
web_scrape()  # Run the web scraping function to populate the database
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('SERVER_HOST')],  
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)
app.include_router(chatbot.router)
app.include_router(api.router, prefix="/api")

app.mount("/style", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "style")), name="style")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

 