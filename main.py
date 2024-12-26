"""
https://dylanbeattie.net/2021/01/12/adding-events-to-google-calendar-via-a-link.html
"""
import urllib.parse
from sender import send_email

BASE_LINK = 'https://calendar.google.com/calendar/u/0/r/eventedit'


def print_menu():
    """
    Prints initial menu and asks user to decide details that will be included with the link.
    """
    print("Welcome to CalendarVAR")
    print("Here you can add a personalized event to your own google calendar \nand create a link to share with friends.")
    print("Choose what details you want to add to your persoalized event \nbelow by entering the number of the choices you wish to add.")
    print("1. One-line summary")
    print("2. Date")
    print("3. Details")
    print("4. Location")
    print("5. Recurrence")
    
    choice = input(">")
    return choice

def get_date():
    """
    Will request date from user and appropriately format date according to the below format
    19980118T230000 -> YYYYMMDDTHHSS00
    """
    start_date_input = input("When will your event be starting? Use the following format 'DD MM YYYY HH SS'\n>")
    end_date_input = input("When will your event be ending? Use the following format 'DD MM YYYY HH SS'\n>")
    
    s_date_list = start_date_input.split()
    e_date_list = end_date_input.split()
    
    start_date = s_date_list[2] + s_date_list[1] + s_date_list[0] + 'T' + s_date_list[3] + s_date_list[4] + '00'
    end_date = e_date_list[2] + e_date_list[1] + e_date_list[0] + 'T' + e_date_list[3] + e_date_list[4] + '00'
    
    date = start_date + '/' + end_date
    return date

def get_recurrence():
    """
    Asks user to decide from a set of recurrence options.
    """
    print("You can choose from the below options for recurrence")
    print("1. Daily")
    print("2. Every other day")
    print("3. Weekly")
    print("4. Every other week")
    print("5. Monthly")
    print("6. Every other month")
    print("7. Actually, nevermind")
    c = input(">")
    
    if c == '7':
        return None
    else:
        count = input("For how many times?\n>")

    if c == '1':
        recurr = "RRULE:FREQ=DAILY;COUNT="
    elif c == '2':
        recurr = "RRULE:FREQ=DAILY;INTERVAL=2;COUNT="
    elif c == '3':
        recurr = "RRULE:FREQ=WEEKLY;COUNT="
    elif c == '4':
        recurr = "RRULE:FREQ=WEEKLY;INTERVAL=2;COUNT="
    elif c == '5':
        recurr = "RRULE:FREQ=MONTHLY;COUNT="
    elif c == '6':
        recurr = "RRULE:FREQ=MONTHLY;INTERVAL=2;COUNT="
    
    return recurr + count
    

def get_params(choice):
    """
    Ask user to enter specifictions of chosen parameters
    """
    print("Now you will be sequentially prompted to enter the details you chose to add to your event.")
    params = []
    for n in choice:
        if n == '1':
            summary = input("Please write a one-line summary of your event below.\n>")
            encoded_summary = urllib.parse.quote_plus(summary)
            params.append('text=' + encoded_summary)
    
        elif n == '2':
            date_str = get_date()
            params.append('dates=' + date_str)

        elif n == '3':
            details = input("Please write the details of your event below.\n>")
            encoded_details = urllib.parse.quote_plus(details)
            params.append('details=' + encoded_details)

        elif n == '4':
            location = input("Please write the address or location of your event below.\n>")
            encoded_location = urllib.parse.quote_plus(location)
            params.append('location=' + encoded_location)

        elif n == '5':
            recurrence = get_recurrence()
            params.append('recur=' + recurrence)

    return params

def main():
    choice = print_menu()
    
    params = get_params(choice)
    
    if params is not None:
        link = BASE_LINK + '?'
        for param in params:
            link += param
            if param != params[-1]:
                link += '&'
    else:
        link = BASE_LINK

    send = input("Would you like to receive this link through email?\n1. Yes\n2. No\n>")
    if send == "1":
        send_email(link)    
    print("Here follows the link to send to your friends!\n\n")
    print(link)

if __name__ == '__main__':
    main()
