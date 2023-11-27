import random
import numpy as np
from pprint import pprint


def generate_random_board():
    # function returns true if piece
    # was placed, false otherwise
    def randomly_place_peice(size):
        is_vertical = random.choice([True, False])
        if is_vertical:
            x, y = random.randint(0, 9), random.randint(0, 9-size+1)
            ship = [[x, y+i] for i in range(size)]
            spaces_are_empty = all(board[x][y] == 0 for x, y in ship)
            while not spaces_are_empty:
                x, y = random.randint(0, 9), random.randint(0, 9-size+1)
                ship = [[x, y+i] for i in range(size)]
                spaces_are_empty = all(board[x][y] == 0 for x, y in ship)

        else:
            x, y = random.randint(0, 9-size+1), random.randint(0, 9-size+1)
            ship = [[x+i, y] for i in range(size)]
            spaces_are_empty = all(board[x][y] == 0 for x, y in ship)
            while not spaces_are_empty:
                x, y = random.randint(0, 9-size+1), random.randint(0, 9)
                ship = [[x+i, y] for i in range(size)]
                spaces_are_empty = all(board[x][y] == 0 for x, y in ship)
        for x, y in ship:
            board[x][y] = 1

    board = [[0]*10 for _ in range(10)]
    randomly_place_peice(5)
    randomly_place_peice(4)
    randomly_place_peice(3)
    randomly_place_peice(3)
    randomly_place_peice(2)
    return board
def initialize_guesses():
    return [(x, y) for x in range(10) for y in range(10)]


def generate_random_guess():
    coords = random.choice(guesses)
    guesses.remove(coords)
    return coords

# this function must store the state of the last guess
# if the last guess was a hit. 
# if the last guess was a hit, then the next guess should be
# adjecent to the last guess
def guess_adjecent_after_hit():
    pass


def is_game_over(board, guesses):
    for r in range(10):
        for c in range(10):
            if board[r][c] == 1 and (r, c) in guesses:
                return False
    return True



if __name__ == '__main__':
    scores = []
    for _ in range(10_000):
        board = generate_random_board()
        guesses = initialize_guesses()
        guess_count = 0
        while not is_game_over(board, guesses):
            x, y = generate_random_guess()
            guess_count += 1
        scores.append(guess_count)

    print(f'{min(scores)=}')
    print(f'{scores.count(100)=}')
    print('Average score: ', np.mean(scores))
