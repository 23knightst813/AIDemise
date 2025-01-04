@echo off
set ROOT_DIR=%~dp0

echo Starting FastAPI in a new terminal...
pushd "%ROOT_DIR%FastAPIy\Api"
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)
echo Activating virtual environment...
call venv\Scripts\activate
echo Installing Python requirements...
pip install -r requirements.txt
start "FastAPI" cmd /k "uvicorn main:app --reload"
popd

echo Starting Svelte dev server in a second terminal...
pushd "%ROOT_DIR%sveltey"
echo Installing npm dependencies...
npm install
start "Svelte" cmd /k "npm run dev"
popd

echo Both processes started in separate terminals!