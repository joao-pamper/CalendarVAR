# CalendarVAR - Add Cruzeiro's next games to Google Calendar

**CalendarVAR** is a Python script that allows you to add the next 5 home and away games of Cruzeiro to google calendar. 

Don't ever miss the next Cruzeiro games by quickly adding the games to your calendar so that you can plan ahead to watch all the games.

---

## Requirements

- Python 3.x
- others found in requirements.txt

---

## Usage

1. Make sure all games are in the db:
   ```bash
   python scrape_games.py

2. Add the games to your google calendar:
   ```bash
   python post_to_calendar.py
