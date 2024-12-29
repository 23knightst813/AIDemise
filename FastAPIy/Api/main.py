from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from AI import gen_scenario, gen_story_result
import uuid
from typing import Dict

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://zz1l696m-5173.uks1.devtunnels.ms"  # Sport forwarded URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store scenarios per session
scenarios: Dict[str, str] = {}

# Session management
def get_session_id():
    return str(uuid.uuid4())


@app.get("/")
def read_root():
    return "Welcome to the AI API. Call /gen_scenario first, then /gen_story_result with your response."


@app.get("/gen_scenario")
def get_scenario():
    session_id = get_session_id()
    scenarios[session_id] = gen_scenario()
    return {
        "session_id": session_id,
        "scenario": scenarios[session_id]
    }

@app.get("/gen_story_result")
def get_story_result(session_id: str, user_response: str):
    if session_id not in scenarios:
        return {"error": "Invalid session or scenario expired"}
    
    scenario = scenarios[session_id]
    story_result = gen_story_result(scenario, user_response)
    return {"story_result": story_result}