from fastapi import FastAPI
from saas import generate_branding_snippet, generate_keywords

app = FastAPI()


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords")
async def generate_snippet_api(prompt: str):
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/generate_snippet_and_keywords")
async def generate_snippet_api(prompt: str):
    keywords = generate_keywords(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": keywords}
