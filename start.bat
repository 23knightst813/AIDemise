@echo off
set ROOT_DIR=%~dp0

:: First Terminal - FastAPI
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
start "FastAPI Backend" /D "%ROOT_DIR%FastAPIy\Api" cmd /k "venv\Scripts\activate && uvicorn main:app --reload"
popd

:: Second Terminal - Svelte 
echo Attempting to start Svelte...
echo Current directory: %CD%
echo Svelte directory: %ROOT_DIR%sveltey
cd "%ROOT_DIR%sveltey"
echo Checking if package.json exists...
if exist "package.json" (
    echo package.json found!
    start "Svelte Frontend" cmd /k "npm install && npm run dev"
) else (
    echo ERROR: package.json not found in %ROOT_DIR%sveltey
    pause
)

echo Process complete!
pause