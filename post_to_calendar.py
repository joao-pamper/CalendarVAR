from pymongo import MongoClient
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_games():
    """
    Will return all games that are in the database and haven't been posted yet
    as a list of dictionaries (documents).
    """
    games = []

    client = MongoClient("localhost", 27017)

    db = client.calendarVAR

    games_db = db.games

    results = games_db.find({"posted" : False})

    if results is None:
        print("No games found.")

    for game in results:
        games.append(game)

    client.close()

    return games


def get_google_creds():
    """
    Will go through google flow to get access/creds to the calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0, open_browser=False)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    return creds


def post_games(google_creds, games: list):
    """
    Will post the games to the google calendar.
    """
    try:
        service = build("calendar", "v3", credentials=google_creds)

        for game in games:
            game_summary = game["team1"] + " x " + game["team2"]

            game_start_datetime, game_end_datetime = get_game_datetime(game)

            event = {
            'summary': game_summary,
            'description': 'Jogo do CABULOSO',
            'start': {
                'dateTime': game_start_datetime,
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': game_end_datetime,
                'timeZone': 'America/Sao_Paulo',
            },
            'reminders': {
                'useDefault': True,
            },
            }
            
            event = service.events().insert(calendarId='primary', body=event).execute()
            print("Successfully added following event to calendar ", event.get('htmlLink'))
            print(event)

            result = update_posted_status(game)


    except HttpError as error:
        print(f"An error occurred: {error}")
        return False

    return True

def update_posted_status(game:dict):
    """
    Will update status of given game to posted.
    """
    client = MongoClient("localhost", 27017)
    db = client.calendarVAR
    games_db = db.games

    query_filter = {'_id' : game["_id"]}
    update_operation = { '$set' : 
        { 'posted' : True }
    }
    result = games_db.update_one(query_filter, update_operation)

    return result

def get_game_datetime(game: dict):
    """
    Will transform the date and time of game into format of RFC3339 
    (https://tools.ietf.org/html/rfc3339)
    """
    sao_paulo_utc_offset = "-03:00"

    game_date = game["game_date"]
    game_day = game_date[0:2]
    game_month = game_date[3:5]
    game_year = game_date[6:]

    game_start_time = game["game_time"]
    game_start_hour = game_start_time[0:2]
    game_minutes = game_start_time[3:]

    game_end_hour = str(int(game_start_hour) + 1)

    start_datetime = game_year +"-"+ game_month +"-"+ game_day +"T"+ game_start_hour +":"+ game_minutes +":00"+ sao_paulo_utc_offset

    end_datetime = game_year +"-"+ game_month +"-"+ game_day +"T"+ game_end_hour +":"+ game_minutes +":00"+ sao_paulo_utc_offset

    return start_datetime, end_datetime


def PostToCalendar(test: bool, games_collection):
    """
    Will check given collection for games that have not been added yet to the database.
    Then proceed to attempt to add them to a user with already given credentials or 
    attempt to login a user.
    """
    google_creds = get_google_creds()

    games = get_games()

    if len(games) < 1:
        print("No games found to be posted.")
    else:

        if test:
            print("These would be the games that would be posted")
            print(games)
        else:
            print("Attempting to post the following games:")
            print(games)
            try:
                post_games(google_creds, games)
            except:
                print("Unable to post the games.")


if __name__ == "__main__":
    PostToCalendar()