"""
Name: 						Anthony Rufin
Panther ID: 				6227314
Class: 						CAP5602 U01C 1255 - Introduction to Artificial Intelligence
Homework: 					HW2 - Game
Due: 						June 30, 2025
What is this program? 		This program is a two player, zero-sum Tic Tac Toe game. It uses the minimax and alpha-beta pruning algorithms to control
                            The AI's moves during it's turn, and compares the time and cost of each algorithm used. It supports a Human vs Ai game and
                            a AI vs Ai game.

"""
from flask import Flask, render_template, request, jsonify
from gameLogic import TicTacToe, get_ai_move

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game(): #Create a new game
    game = TicTacToe()
    game_data = {
        'board': game.board,
        'currentWinner': game.current_winner,
        'minimax_time': game.minimax_time,
        'alphabeta_time': game.alphabeta_time,
        'minimax_calls': game.minimax_calls,
        'alphabeta_calls': game.alphabeta_calls
    }
    return jsonify(game_data)


@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.json
    game = TicTacToe()
    game.board = data['board']
    game.current_winner = data['currentWinner']
    game.minimax_time = data['minimax_time']
    game.alphabeta_time = data['alphabeta_time']
    game.minimax_calls = data['minimax_calls']
    game.alphabeta_calls = data['alphabeta_calls']

    square = int(data['square'])
    player_letter = data['playerLetter']
    algorithm = data['algorithm']
    game_mode = data['gameMode']

    if game_mode == 'human_vs_ai':
        #Human move
        game.make_move(square, player_letter)

        #Check if the game is over after the human player's move
        if game.current_winner or not game.empty_squares():
            game_data = {
                'board': game.board,
                'currentWinner': game.current_winner,
                'minimax_time': game.minimax_time,
                'alphabeta_time': game.alphabeta_time,
                'minimax_calls': game.minimax_calls,
                'alphabeta_calls': game.alphabeta_calls
            }
            return jsonify(game_data)

        #Only proceed to AI move if game isn't over
        ai_letter = 'O' if player_letter == 'X' else 'X'
        ai_move = get_ai_move(game, ai_letter, algorithm)
        game.make_move(ai_move, ai_letter)

    elif game_mode == 'ai_vs_ai':
        #First AI move (X)
        x_move = get_ai_move(game, 'X', algorithm)
        game.make_move(x_move, 'X')

        #Check if game is over after X move
        if not (game.current_winner or not game.empty_squares()):
            #Second AI move (O)
            o_move = get_ai_move(game, 'O', algorithm)
            game.make_move(o_move, 'O')

    game_data = {
        'board': game.board,
        'currentWinner': game.current_winner,
        'minimax_time': game.minimax_time,
        'alphabeta_time': game.alphabeta_time,
        'minimax_calls': game.minimax_calls,
        'alphabeta_calls': game.alphabeta_calls
    }
    return jsonify(game_data)


if __name__ == '__main__':
    app.run(debug=True)