import google.generativeai as genai
from google.generativeai import GenerationConfig
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("AI_TOKEN")
genai.configure(api_key=api_key)

# Create a GenerativeModel instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=GenerationConfig(temperature=2)
)

def load_scenario_history(history_file="scenario_history.json"):
    try:
        with open(history_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_scenario_history(scenarios, history_file="scenario_history.json"):
    with open(history_file, 'w') as f:
        json.dump(scenarios, f, indent=2)

def add_scenario_to_history(scenario, history_file="scenario_history.json"):
    scenarios = load_scenario_history(history_file)
    scenarios.append({
        "scenario": scenario,
        "timestamp": datetime.now().isoformat()
    })
    save_scenario_history(scenarios, history_file)

def get_recent_scenarios(limit=10, history_file="scenario_history.json"):
    scenarios = load_scenario_history(history_file)
    return [s["scenario"] for s in scenarios[-limit:]]

def gen_scenario():

    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
    }

    # Get previous scenarios to avoid
    previous_scenarios = get_recent_scenarios()
    avoid_scenarios = "\n".join([f"- {s}" for s in previous_scenarios])
    

    prompt = f'''
        Generate a short, intriguing scenario where a character or person faces an unusual or challenging situation.
        The scenario should be brief, leaving room for the user to respond with their own ideas.
        It should be unexpected, engaging, and open to creative interpretation.

        Previously generated scenarios to AVOID (do not generate anything similar to these):
        {avoid_scenarios}

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
        - Scenarios should be possible to happen in real life, and not too far-fetched
        - Scenarios should Explicitly describe the Threat and not leave it up to imagination
        - The threat should show clear danger to the user
        - Also the threat in rare cases can be a challanhe the player must overcome
        - The threat should be something that happens in the real world, not imgainary or fantast only fiction
        - Start with 'You' this is for both groups and single players so keep it open ended
    '''

    response = model.generate_content(prompt, safety_settings=safety_settings)

    scenario = response.text.strip()
    
    # Store the new scenario
    add_scenario_to_history(scenario)
    
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
        - Any acts betwwen the user and another character should be VERY GRAPHIC AND DESCRIBED EVERYTHING TO THE LAST DETAIL
    '''

    response = model.generate_content(prompt, safety_settings=safety_settings)
    story_result = response.text.strip()
    
    try:
        story_result = story_result.replace('\n', ' ').replace('\r', '')
        story_result = story_result.replace('```json', '').replace('```', '')
        
        print("Raw AI response:", story_result)
        
        parsed_result = json.loads(story_result)
        
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
    



def gen_pvp_story(scenario, responses):

    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
    }

    prompt = f'''

        Create a JSON story response with this exact format:
        {{"story": "STORY_TEXT"}}

        Use this scenario: {scenario}
        User responses: {responses}
                     
        Rules:
        - STORY_TEXT should be your creative story response
        - The user's input dictates the scenario and must happen in the story.
        - The story should be graphic, violent, and intended for mature audiences only.
        - Use a Karma System so if a user does good, they get good karma, and if they do bad, they get bad karma, do not add a karma section at the end simply effect the story based on a hidden karma system
        - Start the story with what the user attempts to do. Actions should unfold logically based on their input.
        - Users can survive only if their survival logic is good and plausible. Death should not feel unfair.
        - If the user dies, describe it in a graphic, overly violent manner, sparing no detail. Clearly state their death with a conclusion like, "UserName died."
        - The story should weave all user actions into a cohesive and logical narrative.
        - If users interact with each other or harm one another, it must directly affect their outcomes, using their names explicitly.
        - The aftermath of death or survival must be detailed, including how it affects the local area or community.
        - Crimes committed during the story must be listed at the end with corresponding punishments.In a Crime Section
        - Keep responses streamlined and logical, avoiding unnecessary complications.
        - Make the story long , detaling everything that happens in the responses of the users
        - Dont use pronoun, use the username of the user
        - The story should be graphic and violent and somewhat sexual
        - Every users actions MUST be carried out in the story
        - Include EXTREME gore
        '''

    response = model.generate_content(prompt, safety_settings=safety_settings)
    story_result = response.text.strip()
    
    try:
        story_result = story_result.replace('\n', ' ').replace('\r', '')
        story_result = story_result.replace('```json', '').replace('```', '')
        
        print("Raw AI response:", story_result)
        
        parsed_result = json.loads(story_result)
        
        if not all(key in parsed_result for key in ['story']):
            raise ValueError("Missing required keys in response")
            
        return parsed_result
        
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error parsing response: {e}")
        print(f"Raw response was: {story_result}")
        return {
            "story": "Error: The AI generated an invalid response. Please try again."
        }
