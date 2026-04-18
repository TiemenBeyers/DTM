from flask import Flask
import requests

app = Flask(__name__)

BASE_URL = "https://my-json-server.typicode.com/TiemenBeyers/DTM"


def get_teams():
    return requests.get(f"{BASE_URL}/teams").json()


def get_races():
    return requests.get(f"{BASE_URL}/races").json()


# 🏎️ LOGO'S (online links)
LOGOS = {
    "Audi": "https://logo.clearbit.com/audi.com",
    "BMW": "https://logo.clearbit.com/bmw.com",
    "Mercedes-AMG": "https://logo.clearbit.com/mercedes-benz.com",
    "Ferrari": "https://logo.clearbit.com/ferrari.com",
    "Lamborghini": "https://logo.clearbit.com/lamborghini.com",
    "Porsche": "https://logo.clearbit.com/porsche.com"
}


# 🎨 STYLE + BACKGROUND
STYLE = """
<style>
body {
    margin:0;
    font-family: Arial, sans-serif;
    background: url('https://images.unsplash.com/photo-1549921296-3a6b2a5e7e0d') no-repeat center center/cover;
    color: white;
    text-align: center;
}

.overlay {
    background: rgba(0,0,0,0.75);
    min-height: 100vh;
    padding-bottom: 40px;
}

h1 {
    color: #ff2e2e;
    padding-top: 20px;
}

.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
}

.card {
    background: rgba(34,34,34,0.9);
    border-radius: 12px;
    padding: 20px;
    margin: 10px;
    width: 220px;
    box-shadow: 0 0 20px rgba(255,0,0,0.4);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(255,0,0,0.8);
}

img {
    width: 80px;
    height: 80px;
    object-fit: contain;
    margin-bottom: 10px;
    background: white;
    border-radius: 50%;
    padding: 5px;
}

a {
    text-decoration: none;
    color: #00ffcc;
}

.button {
    display: inline-block;
    padding: 10px 20px;
    margin: 15px;
    background: #ff2e2e;
    color: white;
    border-radius: 8px;
    transition: 0.3s;
}

.button:hover {
    background: #ff5555;
}

.small {
    color: #ccc;
    font-size: 14px;
}
</style>
"""


@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>DTM App</title>
        {STYLE}
    </head>
    <body>
        <div class="overlay">
            <h1>🏁 DTM Web App</h1>

            <a class="button" href="/teams">Bekijk Teams</a>
            <a class="button" href="/races">Bekijk Races</a>
        </div>
    </body>
    </html>
    """


@app.route("/teams")
def teams():
    teams = get_teams()

    html = f"""
    <html>
    <head>
        <title>Teams</title>
        {STYLE}
    </head>
    <body>
    <div class="overlay">
    <h1>🏎️ Teams</h1>
    <div class="container">
    """

    for t in teams:
        logo = LOGOS.get(t["manufacturer"], "")
        html += f"""
        <div class="card">
            <img src="{logo}">
            <h3>{t["name"]}</h3>
            <p class="small">{t["manufacturer"]}</p>
            <a href="/teams/{t["id"]}">Details →</a>
        </div>
        """

    html += """
    </div>
    <a class="button" href="/">Home</a>
    </div>
    </body>
    </html>
    """
    return html


@app.route("/teams/<int:id>")
def team_detail(id):
    teams = get_teams()
    team = next((t for t in teams if t["id"] == id), None)
    logo = LOGOS.get(team["manufacturer"], "")

    return f"""
    <html>
    <head>
        <title>{team['name']}</title>
        {STYLE}
    </head>
    <body>
    <div class="overlay">
        <h1>{team['name']}</h1>

        <div class="card" style="margin:auto;">
            <img src="{logo}">
            <p><b>Manufacturer:</b> {team['manufacturer']}</p>
            <p><b>Country:</b> {team['country']}</p>
        </div>

        <a class="button" href="/teams">Terug</a>
    </div>
    </body>
    </html>
    """


@app.route("/races")
def races():
    races = get_races()

    html = f"""
    <html>
    <head>
        <title>Races</title>
        {STYLE}
    </head>
    <body>
    <div class="overlay">
    <h1>🏁 Races</h1>
    <div class="container">
    """

    for r in races:
        html += f"""
        <div class="card">
            <h3>{r['event']}</h3>
            <p class="small">{r['circuit']}</p>
            <p class="small">{r['country']}</p>
        </div>
        """

    html += """
    </div>
    <a class="button" href="/">Home</a>
    </div>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(debug=True)
