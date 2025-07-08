#!/bin/bash
cd /home/joao/CalendarVAR/ || exit 1
source venv-calendarVAR/bin/activate
python3 main.py
deactivate

