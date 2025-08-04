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
import time
import random

class TicTacToe:
    def __init__(self): #Initializes the game state with an empty board and tracking variables
        self.board = [' ' for _ in range(9)] #3x3 board represented as a list
        self.current_winner = None #Tracks the Winner
        self.minimax_time = 0 #Tracks the time spent calculating the best move using minimax
        self.alphabeta_time = 0 #Tracks the time spent calculating the best move using alpha-beta pruning
        self.minimax_calls = 0 #Tracks the total number of minimax calls
        self.alphabeta_calls = 0 #Tracks the total number of alpha-beta calls

    def print_board(self): #Prints the current state of the board to the console.
        for row in [self.board[i * 3:(i + 1) * 3] for i in range (3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums(): #Prints a board with position numbers to show players where to move
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self): #Returns a list of indices of empty squares (available moves)
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self): #Returns true if there are still empty squares on the board
        return ' ' in self.board

    def num_empty_squares(self): #Returns the count of empty squares
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check rows
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check columns
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        if square % 2 == 0:  # The only diagonal positions are 0, 2, 4, 6, 8
            # Top-left to bottom-right diagonal
            first_diagonal = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in first_diagonal]):
                return True
            # Top-right to bottom-left diagonal
            second_diagonal = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in second_diagonal]):
                return True
        return False


def minimax(game, maximizing_player, player_letter):
    """
    This function is the minimax implementation for this program.
    It calculates the best move position and returns a dictionary
    with the best move position and score. It also tracks the
    time it took for the AI to calculate the move and the
    number of calls it needed to make.
    """
    start_time = time.time() #Initializes the timer.
    game.minimax_calls += 1
    opponent_letter = 'O' if player_letter == 'X' else 'X'

    #Code to check if the game has reached the goal state. This is done first in the function call to enusre that the game stops once it has reached a goal state.
    if game.current_winner == player_letter: #If player 1 is the winner
        end_time = time.time()
        game.minimax_time += (end_time - start_time)
        return {'position': None, 'score': 1}
    elif game.current_winner == opponent_letter: #If the ai is the winner
        end_time = time.time()
        game.minimax_time += (end_time - start_time)
        return {'position': None, 'score': -1}
    elif not game.empty_squares(): #If there is a tie
        end_time = time.time()
        game.minimax_time += (end_time - start_time)
        return {'position': None, 'score': 0}

    if maximizing_player: #Iterates through all the possible moves for the Maximizing player.
        best = {'position': None, 'score': -float('inf')}
        for possible_move in game.available_moves(): #This for loop simulates the possible moves the ai could make in the current turn.
            game.make_move(possible_move, player_letter)
            sim_score = minimax(game, False, player_letter)
            game.board[possible_move] = ' ' #Since we are only simulating the possible moves, we undo the move here to return to the current game state
            game.current_winner = None
            sim_score['position'] = possible_move

            if sim_score['score'] > best['score']: #If the move is better than the current score for the ai, we set the move as the next one the ai will use.
                best = sim_score
        end_time = time.time()
        game.minimax_time += (end_time - start_time)
        return best #Returns the best move for this turn
    else:#Iterates through all the possible moves for the Minimizing player.
        best = {'position': None, 'score': float('inf')}
        for possible_move in game.available_moves(): #This for loop simulates the possible moves the ai could make in the current turn.
            game.make_move(possible_move, opponent_letter)
            sim_score = minimax(game, True, player_letter)
            game.board[possible_move] = ' ' #Since we are only simulating the possible moves, we undo the move here to return to the current game state
            game.current_winner = None
            sim_score['position'] = possible_move

            if sim_score['score'] < best['score']: #If the move is better than the current score for the ai, we set the move as the next one the ai will use.
                best = sim_score
        end_time = time.time()
        game.minimax_time += (end_time - start_time)
        return best #Returns the best move for this turn

def alphabeta(game, maximizing_player, player_letter, alpha=-float('inf'), beta=float('inf')):
    """
       This function is the alpha-beta pruning implementation for this program.
       It calculates the best move position and returns a dictionary
       with the best move position and score. It also tracks the
       time it took for the AI to calculate the move and the
       number of calls it needed to make. It uses alpha-beta pruning
       to prune unnecessary branches.
       """
    start_time = time.time() #Like with the minimax algorithm, we create a timer to keep track of how long it takes for the ai to calculate a move.
    game.alphabeta_calls += 1
    opponent_letter = 'O' if player_letter == 'X' else 'X'

    if game.current_winner == player_letter:
        end_time = time.time()
        game.alphabeta_time += (end_time - start_time)
        return {'position': None, 'score': 1}
    elif game.current_winner == opponent_letter:
        end_time = time.time()
        game.alphabeta_time += (end_time - start_time)
        return {'position': None, 'score': -1}
    elif not game.empty_squares():
        end_time = time.time()
        game.alphabeta_time += (end_time - start_time)
        return {'position': None, 'score': 0}

    #Like with the minimax function, we iterate through the moves that the maximizing or minimizing player could make.
    if maximizing_player: #Maximizing Value
        best = {'position': None, 'score': -float('inf')}
        #Like in the minimax function, we make a hypothetical  move, evaluate the position after this move, undo the hypothetical move.
        for possible_moves in game.available_moves():
            game.make_move(possible_moves, player_letter)
            sim_score = alphabeta(game, False, player_letter, alpha, beta)
            game.board[possible_moves] = ' '
            game.current_winner = None
            sim_score['position'] = possible_moves

            if sim_score['score'] > best['score']: #We replace the current best move if the simulated move is better.
                best = sim_score

            alpha = max(alpha, best['score']) #We use the max function to check whether the new best move is better than the current alpha score.
            #But if the minimizing player already has a better option, we will stop exploring this branch since the maximizing player will not choose it.
            if alpha >= beta:
                break

        end_time = time.time()
        game.alphabeta_time += (end_time - start_time)
        return best
    else: #Minimizing Value
        best = {'position': None, 'score': float('inf')}
        #Like in the minimax function, we make a hypothetical  move, evaluate the position after this move, undo the hypothetical move.
        for possible_moves in game.available_moves():
            game.make_move(possible_moves, opponent_letter)
            sim_score = alphabeta(game, True, player_letter, alpha, beta)
            game.board[possible_moves] = ' '
            game.current_winner = None
            sim_score['position'] = possible_moves

            if sim_score['score'] < best['score']:
                best = sim_score

            beta = min(beta, best['score']) #We use the min function to compare the new best move with the current beta score.
            # But if the maximizing player already has a better option, we will stop exploring this branch since the minimizing player will not choose it.
            if alpha >= beta:
                break
        end_time = time.time()
        game.alphabeta_time += (end_time - start_time)
        return best

def get_ai_move(game, player_letter, algorithm):
    """
            Get the AI's move using whichever algorithm the user chose
            Returns a random move if board is empty, otherwise uses the specified algorithm
    """
    if len(game.available_moves()) == 9:
        return random.choice(game.available_moves())

    if algorithm == 'minimax':
        move = minimax(game, True, player_letter)['position']
    else:  # alphabeta
        move = alphabeta(game, True, player_letter)['position']
    return move


