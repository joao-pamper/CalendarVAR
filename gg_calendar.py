import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def authenticate_google_calendar():
    """Shows basic usage of the Google Calendar API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_calendar_event(service, match_info):
    """Create a calendar event for a soccer match."""
    event = {
        'summary': f"{match_info['team1']} vs {match_info['team2']}",
        'description': 'Soccer match.',
        'start': {
            'date': match_info['date']
        #     'dateTime': match_info['date'] + match_info['time'],  # Adjust this to your time format
        #     'timeZone': 'America/Sao_Paulo',
        },
         'end': {
            'date': match_info['date']
        #     'dateTime': match_info['date'] + 'T21:00:00',  # Assuming 2 hours per match
        #     'timeZone': 'America/Sao_Paulo',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},  # Reminder 1 day before
                #{'method': 'popup', 'minutes': 10},  # Reminder 10 minutes before
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")

# Example usage
if __name__ == '__main__':
    service = authenticate_google_calendar()
    
    create_calendar_event(service, match)

