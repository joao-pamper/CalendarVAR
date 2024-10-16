from flask import Flask, request, render_template
from crawler import Fotmob_web_crawler
from gg_calendar import authenticate_google_calendar, create_calendar_event

app = Flask(__name__)

@app.route('/')
def home():
    
    return "Welcome to the soccer calendar app!"

if __name__ == '__main__':
    app.run(debug=True)
