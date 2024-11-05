from gg_calendar import authenticate_google_calendar, create_calendar_event
"""
https://dylanbeattie.net/2021/01/12/adding-events-to-google-calendar-via-a-link.html
"""

def main():
    print()
    print("Welcome to CalendarVAR")
    print()
    print()
    print("Here you can add a personalized event to your own google calendar and create a link to share with friends.")

    print("Please enter you email below:")
    event_name = input("What do you wanna name your event? ")
    print()
    event_time = input("When do you want this event to happen? ")
    print()
    location_choice = input("Is there a specific location you want to include for this event? Y/N ")
    if location_choice.lower() == "y":
        event_location = input("Where? ")
    else:
        event_location = None
    
    
    print("Here follows the link to send to your friends!")
    print(event_link)

    service = authenticate_google_calendar()
    

    create_calendar_event(service,)

if __name__ == '__main__':
    main()
