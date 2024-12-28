REM filepath: /c:/Users/mesh user/Documents/Code/Me/AIDemise/start.bat
@echo off
echo Starting FastAPI in a new terminal...
start "FastAPI" /D "C:\Users\mesh user\Documents\Code\Me\AIDemise\FastAPIy\Api" ^
    "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\python3.11.exe" -m uvicorn main:app --reload

echo Starting Svelte dev server in a second terminal...
start "Svelte" /D "C:\Users\mesh user\Documents\Code\Me\AIDemise\sveltey" cmd /k ^
 "npm install && npm run dev"

echo Both processes were started in separate terminals!