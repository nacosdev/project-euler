import random
import pprint
squares = 'GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2'
squares = squares.split(' ')
board_dict = {}
for item in squares:
    board_dict[item] = 0
pprint.pprint(board_dict)
C = [
    'GO',
    'JAIL',
    'C1',
    'E3',
    'H2',
    'R1',
    'NEXTR',
    'NEXTR',
    'NEXTU',
    'BACK',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
]

CC = [
    'GO',
    'JAIL',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
    'SAME',
]

def calculateProbabilities(sided_dice, board, list_board):
    vueltas = 0
    board['GO'] += 1
    pos_boa = 0
    while vueltas < 1000000:#10000000:
        dice = random.randint(1,sided_dice)
        dice2 = random.randint(1,sided_dice)
        advance = dice + dice2
        new_pos = advance + pos_boa
        if new_pos > 39:
            new_pos = new_pos - 40
        if new_pos in [2,17,33]:#CC
            #aca va CC
            new_square = CC[random.randint(0,15)]
            if new_square is 'SAME':
                new_square = list_board[new_pos]
            board[new_square] += 1
        elif new_pos in [7,22,36]:#CH
            #Aca va CH
            new_square = C[random.randint(0,15)]
            if new_square is 'NEXTR':
                if new_pos is 7:
                    new_pos = 15
                elif new_pos is 22:
                    new_pos = 25
                else:
                    new_pos = 5
                new_square = list_board[new_pos]
            elif new_square is 'NEXTU':
                if new_pos is 7:
                    new_pos = 12
                elif new_pos is 22:
                    new_pos = 28
                else:
                    new_pos = 12
                new_square = list_board[new_pos]
            elif new_square is 'BACK':
                new_pos = new_pos - 3
                new_square = list_board[new_pos]
            elif new_square is 'SAME':
                new_square = list_board[new_pos]
            else:
                new_pos = list_board.index(new_square)
            board[new_square] += 1
        elif new_pos is 30:
            new_pos = 10
            board['JAIL'] += 1
        else:
            board[list_board[new_pos]] += 1
        pos_boa = new_pos
        vueltas += 1
    return board


results_dict = calculateProbabilities(6, board_dict,squares)
pprint.pprint(results_dict)
