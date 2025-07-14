from fastapi import APIRouter, Request
from dotenv import load_dotenv
import httpx
import os 
load_dotenv()
router = APIRouter()

OPENROUTER_API_KEY = os.getenv("OPEN_API_KEY")
MODEL = "mistralai/mistral-7b-instruct"  # or "openai/gpt-3.5-turbo"

@router.post("/chat")
async def chatbot_endpoint(request: Request):
    body = await request.json()
    query = body.get("query", "").strip()

    # Use async HTTP client to call the outlets API
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get("http://localhost:8000/api/outlets")
            response.raise_for_status()
            outlets = response.json().get("outlets", [])
    except Exception as e:
        return {"response": f"Error fetching outlet data: {e}"}

    # Format outlet data into prompt
    context = "\n".join(
        f"Name: {o['name']}, Address: {o['address']}, Email: {o['email']}, "
        f"Telephone: {o['telephone']}, Categories: {o['categories']}, "
        f"Latitude: {o['lat']}, Longitude: {o['lng']}"
        for o in outlets
    )

    messages = [
        {"role": "system", "content": "You are a helpful assistant for McDonald's outlets in Malaysia."},
        {"role": "user", "content": f"{context}\n\nQuestion: {query}"}
    ]

    # Call OpenRouter
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            res = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": MODEL,
                    "messages": messages,
                }
            )
            res.raise_for_status()
            data = res.json()
            answer = data["choices"][0]["message"]["content"].strip()
            return {"response": answer}
    except Exception as e:
        return {"response": f"Chatbot error (OpenRouter): {e}"}
