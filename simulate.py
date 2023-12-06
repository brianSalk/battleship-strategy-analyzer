import random
import numpy as np
from pprint import pprint


def generate_random_board():
    def randomly_place_peice(size, label):
        try:
            assert len(label) == 1
        except AssertionError:
            print('label must be a string of length 1')
            exit()
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
            x, y = random.randint(0, 9-size+1), random.randint(0, 9)
            ship = [[x+i, y] for i in range(size)]
            spaces_are_empty = all(board[x][y] == 0 for x, y in ship)
            while not spaces_are_empty:
                x, y = random.randint(0, 9-size+1), random.randint(0, 9)
                ship = [[x+i, y] for i in range(size)]
                spaces_are_empty = all(board[x][y] == 0 for x, y in ship)
        for x, y in ship:
            board[x][y] = label
        ships[label] = size
        ship_sizes[label] = size
        # END randomly_place_peice
    ships = {}
    ship_sizes = {}
    board = [[0]*10 for _ in range(10)]
    randomly_place_peice(5, 'a')
    randomly_place_peice(4, 'b')
    randomly_place_peice(3, 'c')
    randomly_place_peice(3, 'd')
    randomly_place_peice(2, 'e')
    return board, ships, ship_sizes


def initialize_guesses():
    return [(x, y) for x in range(10) for y in range(10)]


def generate_random_guess(guesses):
    coords = random.choice(guesses)
    guesses.remove(coords)
    return coords


def is_game_over(board, guesses):
    for r in range(10):
        for c in range(10):
            if board[r][c] != 0 and (r, c) in guesses:
                return False
    return True


def play_with_random_guess(n=1_000):
    scores = []
    for _ in range(n):
        # ignore ships and ship_sizes
        board, _, _ = generate_random_board()
        guesses = initialize_guesses()
        guess_count = 0
        while not is_game_over(board, guesses):
            generate_random_guess(guesses)
            guess_count += 1
        scores.append(guess_count)
    return scores

def play_game_with_adjacent_guesses_after_hit():
    hits_stack = []
    board, ships, ship_sizes = generate_random_board()


if __name__ == '__main__':
    scores = play_with_random_guess(n=1_000)
    board = generate_random_board()
    print(board)
    
    print(f'{min(scores)=}')
    print(f'{scores.count(100)=}')
    print('Average score: ', np.mean(scores))
    
