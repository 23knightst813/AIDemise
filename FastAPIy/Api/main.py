from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from AI import gen_scenario, gen_story_result, gen_pvp_story
import uuid
from typing import Dict, List
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session management
def get_session_id():
    return str(uuid.uuid4())

# Store scenarios per session
scenarios: Dict[str, str] = {}

# PvP session state
pvp_scenario = None
pvp_responses = []
pvp_participants = set()

class PvPRequest(BaseModel):
    username: str
    response: str = None

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

@app.post("/join_pvp")
async def join_pvp(request: Request):
    data = await request.json()
    username = data.get('username')
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")
    
    global pvp_scenario, pvp_participants
    if pvp_scenario is None:
        pvp_scenario = gen_scenario()
    pvp_participants.add(username)
    return {
        "scenario": pvp_scenario,
        "total_participants": len(pvp_participants)
    }

@app.post("/submit_pvp_response")
async def submit_pvp_response(request: Request):
    data = await request.json()
    username = data.get('username')
    response = data.get('response')
    
    if not username or not response:
        raise HTTPException(status_code=400, detail="Username and response are required")
    
    global pvp_responses, pvp_participants
    pvp_responses.append({"username": username, "response": response})
    
    all_submitted = len(pvp_responses) == len(pvp_participants)
    if all_submitted:
        story = gen_pvp_story(pvp_scenario, pvp_responses)
        return {
            "status": "complete",
            "story": story["story"],  # Update to use the new response format
            "submissions": len(pvp_responses),
            "total": len(pvp_participants)
        }
    
    return {
        "status": "waiting",
        "submissions": len(pvp_responses),
        "total": len(pvp_participants)
    }

@app.get("/pvp_status")
async def get_pvp_status():
    return {
        "status": "waiting" if len(pvp_responses) < len(pvp_participants) else "complete",
        "submissions": len(pvp_responses),
        "total": len(pvp_participants)
    }