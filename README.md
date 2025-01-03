# AIDemise

A simple AI-based survival scenario game built with FastAPI for the backend and Svelte for the frontend. This project was developed to explore FastAPI (having mostly used Flask before) and to learn the basics of Svelte.

## Purpose

AIDemise is an AI-based survival scenario game where players face intriguing and challenging situations generated by AI. The game aims to provide an engaging and creative experience, allowing players to respond to scenarios and see the outcomes of their decisions.

## Technologies Used

- **Backend**: FastAPI
- **Frontend**: Svelte

## Features

- AI-generated scenarios via `gen_scenario` in `AI.py`
- AI-generated story outcomes via `gen_story_result`
- FastAPI server defined in `main.py`
- Svelte client in `sveltey/src`

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/23knightst813/AIDemise.git
   cd AIDemise
   ```

2. Set up the FastAPI server:
   ```bash
   cd FastAPIy/Api
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the Svelte client:
   ```bash
   cd ../../sveltey
   npm install
   ```

4. Run the application:
   ```bash
   ../start.bat
   ```

5. Open your browser at the address the Svelte dev server prints (default: `http://localhost:5173`).

6. Enjoy the AI-driven survival scenarios!

## Road Map

- Add a multi-player mode

## Architecture

The application consists of two main components:

1. **Backend**: The FastAPI server handles the generation of scenarios and story outcomes using AI. It provides endpoints for generating scenarios, submitting responses, and managing PvP sessions.
2. **Frontend**: The Svelte client provides the user interface for interacting with the game. It communicates with the FastAPI server to fetch scenarios and submit responses.

## Dependencies

- FastAPI
- Svelte
- dotenv
- google-generativeai

## Usage Examples

### Generating a Scenario

To generate a scenario, send a GET request to the `/gen_scenario` endpoint. The response will include a session ID and the generated scenario.

### Submitting a Response

To submit a response to a scenario, send a GET request to the `/gen_story_result` endpoint with the session ID and user response as query parameters. The response will include the generated story outcome.

### Joining a PvP Session

To join a PvP session, send a POST request to the `/join_pvp` endpoint with the username in the request body. The response will include the scenario and the total number of participants.

### Submitting a PvP Response

To submit a response in a PvP session, send a POST request to the `/submit_pvp_response` endpoint with the username and response in the request body. The response will indicate whether the submission is complete or waiting for other players.
