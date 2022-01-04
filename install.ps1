# Run using elevated permissions (eg - Run as Admininstrator)

# Install python requirements (assuming we have Python 3.9.4 installed already)
Set-Location $env:USERPROFILE
python -m venv .venvs\androidtvremote_env
.\.venvs\androidtvremote_env\Scripts\Activate

Set-Location $PSScriptRoot
python -m pip install -e .
