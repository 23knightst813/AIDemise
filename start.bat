@echo off
set ROOT_DIR=%~dp0

echo Starting FastAPI in a new terminal...
pushd "%ROOT_DIR%FastAPIy\Api"
start "FastAPI" cmd /k "python -m uvicorn main:app --reload"
popd

echo Starting Svelte dev server in a second terminal...
pushd "%ROOT_DIR%sveltey"
start "Svelte" cmd /k "npm install && npm run dev"
popd

echo Both processes started in separate terminals!