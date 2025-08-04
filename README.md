# Artificial-Intelligence-Course---Tic-Tac-Toe

Name: 						  Anthony Rufin
Panther ID: 				6227314
Class: 						  CAP5602 U01C 1255 - Introduction to Artificial Intelligence
Homework: 					HW2 - Game
Due: 						    June 30, 2025
What is this program? 		This program is a two player, zero-sum Tic Tac Toe game. It uses the minimax and alpha-beta pruning algorithms to control the AI's moves during it's turn, and compares the time and cost of each algorithm used. It supports a Human vs Ai game and a AI vs Ai game. 

File Structure:
HW1-Search:
	templates/
		index.html -> This is the html file holding the main html code for the flask web application
	app.py -> This is the main project file, used to host the flask program.
	gameLogic.py -> This file holds the logic for both the tic tac toe game and the ai algorithms (minimax and alpha-beta pruning)
	run.py -> A Helper file used to create the app.route for the executable file.

Use the run.exe to run the program.

To generate a new run.exe, run the run.py file with all the files listed in the project structure above, and run the following command: pyinstaller --onefile --add-data "templates;templates"  run.py
The new run.py will generate in a new folder called "dist", and will be an executable called run.exe. Note that to create a new executable, the project should follow the same file structure as seen above.

Libraries used:
Flask - For creating the web application, uses Flask, render_template, request, jsonify
time - For keeping track of how long it takes for the AI to make a decision for each algorithm
random - To let the AI randomly select a move at the start of an AI vs Ai game

------------------------------------------------------------------------------------------------------------------------------------------------

index.html
This is the main html page for the program. Note that running the index.html by itself will only load the page template, rather than the full game.

------------------------------------------------------------------------------------------------------------------------------------------------

app.py
app.py is the main file for this project. Like the previous project, it uses flask to create a web applicaton to host the tic tac toe game. app.py has three routes @app.route('/')
def home():, @app.route('/new_game', methods=['POST'])
def new_game():, @app.route('/make_move', methods=['POST'])
def make_move():. The first is solely to render the index.html template, which contains the frontend code for the tic tac toe game. The second, new_game(), initializes the game with the following parameters: What game mode to use (human vs ai or ai vs ai) and what algorithm to use for the ai (minimax or alpha-beta pruning). The third route, make_move(), handles the player's moves and processes the ai's response. This uses the position where the player moved, the currend board state, and the algorithm to use to calculate the best move to counter the player and minimize the overall score. jsonify is used here to handle the board state, winner info, and ai moves. 

------------------------------------------------------------------------------------------------------------------------------------------------

gameLogic.py
gameLogic.py is the main file for the tic tac toe game logic. It contains the classs TicTacToe, and imports the time and random libraries. 
First, there is the constructor function for this class. This is used to initialize the game state with an empty 3x3 board and create the variables we want to track, which are, the current winner of the game, the amount of calls each ai algorithm does, and the time it takes for each ai algorithm to calculate the best move. 
Next is the print_board and print_board_nums functions. print_board is used to print the board to the console, and print_board_nums shows the position numbers of each tile in the board. 
available_moves() returns a list of indices for which moves are available. As in, the list of squares that do not have an X or an O on them already. empty_squares() Returns true if there are still empty squares on the board. 
num_empty_squares() returns the count of empty squares.
make_move() is a function used to check if the tile clicked on is empty and can be filled with an X or an O.

winner(self, square, letter) is a function used to check if any plater (either the human player or the ai) has made a move that caused the game to reach a goal state. It checks the rows, columns and diagonals containing the last move and returns true if it finds a winning line.

------------------------------------------------------------------------------------------------------------------------------------------------

gameLogic.py AI functions:
The program also calls for an implementation of the Minimax and Alpha-Beta pruining algorithms. 

minimax(game, maximizing_player, player_letter) is the function used for implementing the minimax algorithm for this program. It uses the current game state, the player and a boolean to determine whether we are maximizing or minimizing (assuming we are using ai vs ai mode. otherwise, the ai will try to minimize the human player's score). First the program checks to see if the game has already reached the goal state. If so, it checks which player won and returns the result of the game (1 if the human player/player 1 ai won, -1 if the player 2 ai won, and 0 if the game resulted in a draw).
 
However, if the game has not reached the end state, it then calculates the current best move for the ai. First, it checks if the ai is the maximizing player or minimizing player. Then, it iterates through every possible move the ai could make for that turn, comparing them to the current best move (initially, the current best move will be negative or positive infinity respectively). If it finds a better move in its many iterations, it replaces the best move with the new move. It will keep iterating until it checks every possible move, in which case, it returns the best move along with adding the time it took to find the move to the game timer. 


alphabeta(game, maximizing_player, player_letter, alpha=-float('inf'), beta=float('inf')): is the function used for implementing the alpha-beta pruining algorithm for this program. It uses the current game state, the player letter, along with an alpha and beta score. Like the minimax function, we first check to see if the game has already reached the goal state, and return the corresponding score depending on who won the game. Then, we iterate through the moves the ai could make to find the best possible move it can do this turn. 

However, unlike the minimax function, we compare the move to the current alpha or beta score (depending if we are checking the maximizing or minimizing player's next move), and check to see if there is already a better option for the ai in a previous branch. If there is, we prune the branch by breaking from the for loop. 

Lastly, there is get_ai_move(game, player_letter, algorithm):. This function only exists to get the ai's next move, returning a random move if the board is empty. Otherwise, it calls for whichever algorithm is being used for this game. 

