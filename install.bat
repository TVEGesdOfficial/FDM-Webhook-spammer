@echo off
title installing requirements
pip install -r requirements.txt
timeout /t 2 >nul
goto spammer
:spammer
title FDM spammer
python Main.pyc