@echo off
SETLOCAL

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Run the test suite
echo Running test suite...
pytest
SET RESULT=%ERRORLEVEL%

REM Deactivate the virtual environment
call venv\Scripts\deactivate.bat

REM Return exit code
IF %RESULT% EQU 0 (
    echo  passed.
    exit /B 0
) ELSE (
    echo failed.
    exit /B 1
)
