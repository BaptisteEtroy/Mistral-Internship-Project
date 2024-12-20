from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from Mistral.routes import router
from fastapi import Request

app = FastAPI(title="Mistral Q&A Service", version="0.1.0")

# Setup templates
templates = Jinja2Templates(directory="Mistral/templates")

# Include the router that handles queries and other
app.include_router(router)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health_check():
    return {"status": "ok"}
