from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'your_api_key'
BASE_URL = 'https://api.football-data.org/v4/competitions/PL/standings'

def get_premier_league_standings():
    headers = {
        'X-Auth-Token': API_KEY
    }
    try:
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        standings = data['standings'][0]['table']
        return [
            {
                "team": team['team']['name'],
                "points": team['points'],
                "position": team['position']
            }
            for team in standings
        ]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

@app.route('/')
def home():
    standings = get_premier_league_standings()
    return render_template('index.html', standings=standings)

if __name__ == '__main__':
    app.run(debug=True)
