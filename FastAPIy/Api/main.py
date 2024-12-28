from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AI import gen_scenario, gen_story_result

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store current scenario in memory
current_scenario = None

@app.get("/")
def read_root():
    return "Welcome to the AI API. Call /gen_scenario first, then /gen_story_result with your response."

@app.get("/gen_scenario")
def get_scenario(): 
    global current_scenario
    current_scenario = gen_scenario()
    return {"scenario": current_scenario}

@app.get("/gen_story_result")
def get_story_result(user_response: str):
    if not current_scenario:
        return {"error": "Please generate a scenario first using /gen_scenario"}
    
    story_result = gen_story_result(current_scenario, user_response)
    return {"story_result": story_result}