import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class WebhookRequest(BaseModel):
    aqi_level: int
    warning_message: str

class ResponseData(BaseModel):
    status: str
    message: str

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.post("/webhook", response_model=ResponseData)
async def webhook(request: WebhookRequest):
    print("Received aqi level: ", request.aqi_level)
    print("Received warning message: ", request.warning_message)
    return ResponseData(status="success", message="Webhook received")

if __name__ == "__main__":
    uvicorn.run("n8n_microservice:app", host="0.0.0.0", port=8000, reload=True)

