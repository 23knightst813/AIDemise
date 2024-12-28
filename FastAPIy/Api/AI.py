import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load the API key from the .env file
load_dotenv()
# Set the API key
api_key = os.getenv("AI_TOKEN")
# Configure the API with the API key
genai.configure(api_key=api_key)
# Create a GenerativeModel instance
model = genai.GenerativeModel("gemini-1.5-flash")

def gen_scenario():
    response = model.generate_content(''' 
        Generate a short, intriguing scenario where a character or person faces an unusual or challenging situation.
        The scenario should be brief, leaving room for the user to respond with their own ideas.
        It should be unexpected, engaging, and open to creative interpretation.
        Example responses:
        'A tidal wave of rabbits is about to block out the sun and eat you.'
        'You’re trapped in a room that’s filling with jelly, and you must escape before it reaches your head.'
        'A giant chicken is chasing you, and you have only a spoon to defend yourself.'
        The scenario should set the stage for the user to add their own response and decide what happens next.
    ''')
    scenario = response.text
    return scenario

def gen_story_result(scenario, user_response):
    response = model.generate_content(f'''
        Imagine you are an AI tasked with creating a story.
        Here's the scenario: {scenario}
        User Input: {user_response}
        Write a compelling narrative with twists and turns,
        and be sure to evaluate the choices the user might make.
        Clearly state if the user dies or not, 
        and provide a satisfying conclusion to the story.
        keep it short, sweet, and bizarre it should be fairly challenging for the user to survive.

        Provide the story in JSON:
        {{
            "result": "<short bizarre story>",
            "alive": "<true or false>"
        }}
    ''')
    story_result = response.text
    try:
        return json.loads(story_result)
    except json.JSONDecodeError:
        return {"result": "Error parsing response", "alive": False}
