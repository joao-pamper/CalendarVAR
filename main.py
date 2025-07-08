from post_to_calendar import PostToCalendar
from scrape_games import ScrapeGames
import sys
import datetime
from pymongo import MongoClient

#database specifications to be used
GAMES_COLLECTION = "games"
CALENDAR_VAR_DB = "calendarVAR"


def main():
    old_stdout = sys.stdout
    log_file = open("calendarVAR.log","w")
    sys.stdout = log_file
    
    print(datetime.datetime.now())
    
    pa = sys.argv
    try:
        # attempt to connect/create db and collection
        client = MongoClient("localhost", 27017)
        db_calendarVAR = client.calendarVAR
        games_collection = db_calendarVAR.games
    except:
        print("ERROR: Unable to connect to mongodb succesfully.")

    if len(pa) > 1 and pa[1] == "t":
        test = True
        print("TESTING")
        sys.stdout = old_stdout
        print("TESTING")
        print("Running scripts...")

        ScrapeGames(test, games_collection)
        PostToCalendar(test, games_collection)

        print("Finished running!")
        print("Test succesfull")
        sys.stdout = log_file
        print("Test succesfull")

    else:
        test = False
        print("Running scripts...")
        ScrapeGames(test, games_collection)
        PostToCalendar(test, games_collection)
        print("Finished running!")
    
    client.close()

    sys.stdout = old_stdout

    log_file.close()


if __name__ == "__main__":
    main()
