from flask import Flask
import requests

app = Flask(__name__)

# ⚠️ PAS DIT AAN NAAR JOUW GITHUB
BASE_URL = "https://my-json-server.typicode.com/TiemenBeyers/DTM"


def get_teams():
    return requests.get(f"{BASE_URL}/teams").json()


def get_races():
    return requests.get(f"{BASE_URL}/races").json()


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>DTM App</title>
        <style>
            body {
                background:#111;
                color:white;
                text-align:center;
                font-family:Arial;
            }
            a {
                color:#00ffcc;
                display:block;
                margin:10px;
                font-size:20px;
            }
            h1 {
                color:#ff4444;
            }
        </style>
    </head>
    <body>
        <h1>DTM Web App</h1>
        <a href="/teams">Bekijk Teams</a>
        <a href="/races">Bekijk Races</a>
    </body>
    </html>
    """


@app.route("/teams")
def teams():
    teams = get_teams()

    html = """
    <html>
    <head><title>Teams</title></head>
    <body style="background:#111;color:white;text-align:center;">
    <h1>Teams</h1>
    """

    for t in teams:
        html += f'<p><a href="/teams/{t["id"]}">{t["name"]} ({t["manufacturer"]})</a></p>'

    html += '<br><a href="/">Home</a></body></html>'
    return html


@app.route("/teams/<int:id>")
def team_detail(id):
    teams = get_teams()
    team = next((t for t in teams if t["id"] == id), None)

    return f"""
    <html>
    <body style="background:#111;color:white;text-align:center;">
    <h1>{team['name']}</h1>
    <p><b>Manufacturer:</b> {team['manufacturer']}</p>
    <p><b>Country:</b> {team['country']}</p>

    <br><a href="/teams">Terug</a>
    </body>
    </html>
    """


@app.route("/races")
def races():
    races = get_races()

    html = """
    <html>
    <body style="background:#111;color:white;text-align:center;">
    <h1>Races</h1>
    """

    for r in races:
        html += f"<p>{r['event']} - {r['circuit']} ({r['country']})</p>"

    html += '<br><a href="/">Home</a></body></html>'
    return html


if __name__ == "__main__":
    app.run(debug=True)
