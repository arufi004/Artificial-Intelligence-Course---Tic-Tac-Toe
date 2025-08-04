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
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)