from fastapi import FastAPI
import socketio

# Setup FastAPI
app = FastAPI()

# Setup Socket.IO (Async)
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
def read_root():
    return {"Status": "API is running", "Service": "Health App Backend"}

@sio.event
async def connect(sid, environ):
    print("Client connected", sid)

# Nanti jalankan dengan: uvicorn main:socket_app --reload