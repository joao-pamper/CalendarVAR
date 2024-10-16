import requests
from bs4 import BeautifulSoup

def Cruzeiropedia_crawler(url):

    # Send a GET request to fetch the page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # List to store matches
        matches = []

        # Set to track added dates
        #dates_set = set()

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the match blocks (you might need to inspect the structure to adjust the selector)
        match_blocks = soup.find_all("table", width="450px")  # Example class name for match containers

        # Iterate through each match and extract the details
        for match in match_blocks:
            # Extract the teams and date (adjust these based on the actual HTML structure)
            teams = match.find_all("a", class_="mw-redirect")  # Adjust selector for teams
            date = match.find("b")  # Adjust selector for date
            #time = match.find("div", class_="css-hytar5-TimeCSS")  # Adjust selector for date

            print("here")
            # Print the match information
            if teams and date and (len(teams) == 2):
                
                match_info = {
                    "team1": teams[0].text.strip(),
                    "team2": teams[1].text.strip(),
                    "date": date.text.strip(),
                    #"time": format_time(time.text.strip()),
                    #"end_time": end_time(format_time(time.text.strip()))
                }
                # if date not in dates_set:
                #     matches.append(match_info)
                #     dates_set.add(date)  # Add the date to the set

                #Uncomment to DEBUG    
                #     print(f"Match: {teams[0].text.strip()} vs. {teams[1].text.strip()} on {date.text.strip()}")
                # else:
                #    print(f"Duplicate match found for date: {date}")
                return matches
            
def scrape_match_info(url):
    # Send a GET request to fetch the HTML content
    response = requests.get(url)
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing the match info (you might want to specify an id or class if needed)
    table = soup.find('table')
    
    # Extract date, time, and match type (found in the first td element with colspan="3")
    match_info = table.find('td', colspan="3").get_text(separator=" ").strip()
    
    # Extract team names from the second row (in the <small> tags within the <td> elements)
    teams = table.find_all('small')
    team1 = teams[0].get_text().strip()  # Team 1 (Libertad)
    team2 = teams[1].get_text().strip()  # Team 2 (Cruzeiro)
    
    # Return the match information in a dictionary format
    return {
        "match_info": match_info,
        "team1": team1,
        "team2": team2
    }

def main():
    
    url = "https://cruzeiropedia.org/Página_principal"
    #matches = Cruzeiropedia_crawler(url)
    #[{'team1': 'Libertad', 'team2': 'Cruzeiro', 'date': 'Fri, Sep 20', 'time': '12:30AM'}]

    #print(matches)
    # for match in matches:
    #    print(f"{match['team1']} vs {match['team2']} on {match['date']} at {match['time']}")

    match_data = scrape_match_info(url)

    print(match_data)

main()