@echo off
REM -- activate venv --
call "%~dp0\venv\Scripts\activate.bat"

REM -- launch watcher --
start "Watcher" cmd /k "python "%~dp0watch_folder.py""

REM -- launch server --
start "Server" cmd /k "python "%~dp0app.py""

echo.
echo Press any key to STOP watcher + server…
pause > nul

REM -- kill all python processes --
taskkill /f /im python.exe > nul 2>&1