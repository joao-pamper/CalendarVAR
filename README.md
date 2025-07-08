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


1. Download and activate mongodb Community edition on your machine. Use link below for help.    
https://www.mongodb.com/docs/manual/administration/install-community/

2. Start a python venv by running the following command while in the root directory of the folder of this project.
   ```bash
   python3 -m venv venv-calendarVAR
   ```

3. Activate the venv by running the following.
   ```bash
   source venv-calendarVAR/bin/activate
   ```

   Run the following to deactivate the venv if wanted 
   ```bash
   deactivate
   ```

4. Install all required packages by running the following
   ```bash
   python3 -m pip install -r requirements.txt
   ```

5. If you want to connect to your personal google calendar, you will need to take some extra steps to get the credentials.json file, see the link below for more details
https://developers.google.com/workspace/calendar/api/quickstart/python 


6. If you want to first test the scraper, make sure everything is running smoothly and login with google to save your credentials locally run the following
   ```bash
   python3 main.py t
   ```


7. To run the script once use the below command 
   ```bash
   python3 main.py
   ```

8. To set up the cron job by using the cronfile run the following