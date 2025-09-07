from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from chatbot import TeamChatbot
import uvicorn

app = FastAPI()
chatbot = TeamChatbot("Bravo Team")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get('message', '')
    response = chatbot.get_response(message)
    return JSONResponse(content={"response": response})

if __name__ == "__main__":
    uvicorn.run("chatbot_fastapi:app", host="0.0.0.0", port=5000, reload=True)
