$ProjectPath = "C:\vantara-customer-intelligence"
$PythonPath = "$ProjectPath\.venv\Scripts\python.exe"

if (!(Test-Path $PythonPath)) {
    Write-Host "Virtual environment not found!" -ForegroundColor Red
    exit
}

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "Set-Location '$ProjectPath'; & '$PythonPath' -m uvicorn api.main:app --reload --port 8000"
)

Start-Sleep -Seconds 3

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "Set-Location '$ProjectPath'; & '$PythonPath' -m streamlit run frontend/app.py"
)

Write-Host "VANTARA services are starting..." -ForegroundColor Green
Write-Host "API: http://127.0.0.1:8000"
Write-Host "API Docs: http://127.0.0.1:8000/docs"
Write-Host "Dashboard: http://localhost:8501"
