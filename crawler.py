import requests
from bs4 import BeautifulSoup

def Fotmob_web_crawler(url):

    # Send a GET request to fetch the page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # List to store matches
        matches = []

        # Set to track added dates
        dates_set = set()

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the match blocks (you might need to inspect the structure to adjust the selector)
        match_blocks = soup.find_all("a", class_="css-jiwnw2-FtContainer")  # Example class name for match containers

        # Iterate through each match and extract the details
        for match in match_blocks:
            # Extract the teams and date (adjust these based on the actual HTML structure)
            teams = match.find_all("span", class_="css-zyagr9-TeamName")  # Adjust selector for teams
            date = match.find("span", class_="css-majyto-StartDate")  # Adjust selector for date
            time = match.find("div", class_="css-hytar5-TimeCSS")  # Adjust selector for date

            
            # Print the match information
            if teams and date and (len(teams) == 2) and time:
                
                match_info = {
                    "team1": teams[0].text.strip(),
                    "team2": teams[1].text.strip(),
                    "date": format_date(date.text.strip()),
                    #"time": format_time(time.text.strip()),
                    #"end_time": end_time(format_time(time.text.strip()))
                }
                if date not in dates_set:
                    matches.append(match_info)
                    dates_set.add(date)  # Add the date to the set

                #Uncomment to DEBUG    
                    print(f"Match: {teams[0].text.strip()} vs. {teams[1].text.strip()} on {date.text.strip()}")
                else:
                   print(f"Duplicate match found for date: {date}")
                return matches

                
                    
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    return
    
def format_date(date_str):
    """
    Reformats date from 'Fri, Sep 20' to 'yyyy-mm-dd'
    """
    months = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05',
        'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10',
        'Nov': '11', 'Dec': '12'
    }
    
    # Split the date string
    parts = date_str.split(', ')
    month_day = parts[1].split(' ')
    month_str = month_day[0]
    day_str = month_day[1]
    
    # Convert month and day to the desired format
    month = months[month_str]
    day = day_str.zfill(2)  # Ensure day is zero-padded to 2 digits
    
    # Construct the formatted date
    reformatted_date = f"2024-{month}-{day}"
    
    return reformatted_date

def format_time(time_str):
    """
    Reformats time from 12:30AM to T12:30:00
    """
    # Extract AM/PM and the time part
    period = time_str[-2:].upper()  # Get 'AM' or 'PM'
    time_part = time_str[:-2]  # Get '12:30'

    # Split hours and minutes
    hours, minutes = time_part.split(':')
    hours = int(hours)

    # Convert to 24-hour format
    if period == 'AM':
        if hours == 12:  # 12AM is midnight (00:xx)
            hours = 0
    elif period == 'PM':
        if hours != 12:  # Convert PM hours except for 12PM (noon)
            hours += 12

    # Format the time to 'T12:30:00'
    reformatted_time = f"T{str(hours).zfill(2)}:{minutes}:00"
    
    return reformatted_time

def end_time(start_time):
    #Get hour from start time
    start_hour = start_time[1:3]

    #Add two hours and convert to used format
    end_hour = str(int(start_hour) + 2)
    end_time = "T" + end_hour + start_time[3:]

    return end_time

def main():
    
    url = "https://www.fotmob.com/teams/9781/fixtures/cruzeiro"
    matches = Fotmob_web_crawler(url)
    #[{'team1': 'Libertad', 'team2': 'Cruzeiro', 'date': 'Fri, Sep 20', 'time': '12:30AM'}]

    print(matches)
    # for match in matches:
    #    print(f"{match['team1']} vs {match['team2']} on {match['date']} at {match['time']}")

main()