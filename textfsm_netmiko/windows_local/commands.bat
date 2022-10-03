@REM create venv
python -m venv venv

@REM activate venv
venv\Scripts\activate.bat

@REM run script
(venv) λ python windows_local\show_ip_interface_brief.py