
from flask import Flask, render_template, request, redirect, url_for
import random
import psycopg2

app = Flask(__name__)



global player_names
player_names = []

player_roles = {}
player_scores = {
    'player1': 0,
    'player2': 0,
    'player3': 0,
    'player4': 0
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/play", methods=["POST", "GET"])
def play():
    if request.method == "POST":
        return render_template("user.html")

@app.route("/start", methods=["POST", "GET"])
def start():
    if request.method == "POST":
        player1 = request.form["first"]
        player2 = request.form["second"]
        player3 = request.form["third"]
        player4 = request.form["forth"]
        player_names.extend([player1, player2, player3, player4])
        return render_template('index.html', player_names=player_names, player_scores=player_scores)
    return redirect(url_for("play"))

@app.route('/draw_roles', methods=['POST'])
def draw_roles():
    roles = ['RAJA', 'MANTRI', 'SIPAHI', 'CHOR']
    random.shuffle(roles)
    player_roles.update({
        'player1': roles[0],
        'player2': roles[1],
        'player3': roles[2],
        'player4': roles[3],
    })
    for player, role in player_roles.items():
        if role == 'RAJA':
            player_scores[player] += 1000
        elif role == 'MANTRI':
            player_scores[player] += 800

    return render_template('index.html', player_names=player_names, player_roles=player_roles, player_scores=player_scores, guess_section=True)

@app.route('/guess_chor', methods=['POST'])
def guess_chor():
    guess = request.form.get('guess')
    mantri = [player for player, role in player_roles.items() if role == 'MANTRI'][0]
    chor = [player for player, role in player_roles.items() if role == 'CHOR'][0]
    sipahi = [player for player, role in player_roles.items() if role == 'SIPAHI'][0]

    if guess == chor:
        player_scores[sipahi] += 500
        result = "Correct! You found the Chor."
    else:
        result = f"Incorrect! The Chor was {chor}"
        player_scores[chor] += 500
    print(player_scores)
    # save_game_results()
    return render_template('index.html', player_names=player_names, player_roles=player_roles, player_scores=player_scores, result=result)

@app.route('/exit_game')
def exit_game():
    global player_scores
    player_scores = {
        'player1': 0,
        'player2': 0,
        'player3': 0,
        'player4': 0
    }
    return redirect(url_for('home'))  # Redirect to a desired page



if __name__ == '__main__':
    app.run(debug=True)
