# AIDemise

A AI-based survival scenario game built with FastAPI for the backend and Svelte for the frontend. This project was developed to explore FastAPI (having mostly used Flask before) and to learn the basics of Svelte.

## Purpose

AIDemise is an AI-based survival scenario game where players face intriguing and challenging situations generated by AI. The game aims to provide an engaging and creative experience, allowing players to respond to scenarios and see the outcomes of their decisions.

## Technologies Used

- **Backend**: FastAPI
- **Frontend**: Svelte

## Features

- AI-generated scenarios via `gen_scenario` in `AI.py`
- AI-generated story outcomes via `gen_story_result`
- AI-generated Multiplayer Storys/outcomes `join_pvp` , `Submit_pvp_response` , `get_pvp_status`
- FastAPI server defined in `main.py`
- Svelte Front End, allowing users to access single player and multiplayer functionalitys `sveltey/src`

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/23knightst813/AIDemise.git
   cd AIDemise
   ```

2. Set up the servers:
   run `start.bat`

3. Enter your Gemni AI Key in the python `.env`

4. Enter the Fast API server adress in the svelte `.env` (default: `http://localhost:8000`).
   
5. Open your browser at the address the Svelte dev server prints (default: `http://localhost:5173`).

6. Enjoy the AI-driven survival scenarios!

## Architecture

The application consists of two main components:

1. **Backend**: The FastAPI server handles the generation of scenarios and story outcomes using AI. It provides endpoints for generating scenarios, submitting responses, and managing PvP sessions.
2. **Frontend**: The Svelte client provides the user interface for interacting with the game. It communicates with the FastAPI server to fetch scenarios and submit responses.

## Dependencies

- FastAPI
- Svelte
- dotenv
- google-generativeai
