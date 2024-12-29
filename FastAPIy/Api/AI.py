import google.generativeai as genai
from google.generativeai import GenerationConfig
from google.generativeai.types import HarmCategory, HarmBlockThreshold
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
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=GenerationConfig(temperature=1.5)
)

def gen_scenario():
    response = model.generate_content(''' 
        Generate a short, intriguing scenario where a character or person faces an unusual or challenging situation.
        The scenario should be brief, leaving room for the user to respond with their own ideas.
        It should be unexpected, engaging, and open to creative interpretation.
        Example responses:
        'A tidal wave of rabbits is about to block out the sun and eat you.'
        'You’re trapped in a room that’s filling with jelly, and you must escape before it reaches your head.'
        'A giant chicken is chasing you, and you have only a spoon to defend yourself.'
        'A mysterious fog envelops your town, and people start disappearing one by one.'
        'You wake up to find that gravity has reversed, and you must navigate an upside-down world.'
        'A talking cat offers you a deal that could change your life forever.'
        The scenario should set the stage for the user to add their own response and decide what happens next.
        Rules:
        - Do not end with "what do you do?" or similar prompts as this is hardcoded
        - Keep the scenario engaging and open-ended
        - Try to include overly graphic or violent scenarios
        
    ''')  
    scenario = response.text
    return scenario

def gen_story_result(scenario, user_response):
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
    }

    prompt = f'''
        Create a JSON story response with this exact format:
        {{"result": "STORY_TEXT", "alive": BOOLEAN}}

        Use this scenario: {scenario}
        User input: {user_response}

        Rules:
        - STORY_TEXT should be your creative story response
        - Replace BOOLEAN with true or false based on if user survives
        - Use escaped quotes for strings
        - Story should be engaging and creative
        - Story should be related to the scenario
        - The users input must happen
        - Story Should be graphic and viloent and only for only mature audiences
        - The user must have  a low chance of survival but if their survival logic is good, they can survive, and it should not seem unfair
        - what ever the user inputted must happen
        - Keep json structure exact
        - If the user dies, the death should be as graphic and as overally violent as possible
        - Start the story with "You" and then what happens or the user trys to do
    '''

    response = model.generate_content(prompt, safety_settings=safety_settings)
    story_result = response.text.strip()
    
    try:
        # Try to clean up common JSON formatting issues
        story_result = story_result.replace('\n', ' ').replace('\r', '')
        story_result = story_result.replace('```json', '').replace('```', '')
        
        # Print for debugging
        print("Raw AI response:", story_result)
        
        parsed_result = json.loads(story_result)
        
        # Validate expected keys exist
        if not all(key in parsed_result for key in ['result', 'alive']):
            raise ValueError("Missing required keys in response")
            
        return parsed_result
        
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error parsing response: {e}")
        print(f"Raw response was: {story_result}")
        return {
            "result": "Error: The AI generated an invalid response. Please try again.",
            "alive": False
        }