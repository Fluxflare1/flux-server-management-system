@echo off
REM Setup environment for Windows

echo Setting up environment for Windows...
REM Example command for Python virtual environment
python -m venv env
call env\Scripts\activate

REM Install dependencies based on requirements.txt
pip install -r requirements.txt
echo Environment setup complete.
