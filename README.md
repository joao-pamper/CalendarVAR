# CalendarVAR - Add Cruzeiro's next games to Google Calendar

**CalendarVAR** is a Python script that allows you to add the next 5 home and away games of Cruzeiro to google calendar. 

Don't ever miss the next Cruzeiro games by quickly adding the games to your calendar so that you can plan ahead to watch all the games.

---

## Requirements

- Python 3.x
- MongoDB
- others found in requirements.txt

---

## Basic Usage

1. Make sure MongoDB is running on the background.    

2. Activate the web scraper to collect next 5 away and home games from Cruzeiro and add them to the "games" collection, within the "calendarVAR" database by running the following command:    
   ```bash
   python scrape_games.py
   ```
3. Add the games that haven't been flagged as added to your google calendar by running the following command:
   ```bash
   python post_to_calendar.py
   ```
