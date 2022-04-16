from flask import render_template, request
from app import app
from models.game import *
from models.player import *

@app.route('/')
def home():
    return "Rock, Paper, Scissors!"

@app.route('/newgame')
def index():
    return render_template('index.html', title='Home')

@app.route('/playgame', methods=['POST'])
def play_game():
    player1 = Player("Laura", request.form['choice1'])
    player2 = Player("Derek", request.form['choice2'])
    game = Game(player1, player2)
    new_game(game)

    return render_template('results.html', title = "results", game=game)



