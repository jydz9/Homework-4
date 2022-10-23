import copy
import math
import time
from turtle import position

def heuristic(board,player):
    heur = 0
    if player == "X":
        me = "X"
        opponent = "O"
    else:
        me = "O"
        opponent = "X"

    #I win
    #horizontal
    for i in range(0,5):
        for j in range(0,3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == me:
                return 1000

    #vertical
    for i in range(0,2):
        for j in range(0,6):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == me:
                return 1000

    #diagonal
    for i in range(0,2):
        for j in range(0,3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == me:
                return 1000
    
    for i in range(3,5):
        for j in range(0,3):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == me:
                return 1000

    #My opponent wins
    #horizontal
    for i in range(0,5):
        for j in range(0,3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == opponent:
                return -1000

    #vertical
    for i in range(0,2):
        for j in range(0,6):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == opponent:
                return -1000

    #diagonal
    for i in range(0,2):
        for j in range(0,3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == opponent:
                return -1000
    
    for i in range(3,5):
        for j in range(0,3):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == opponent:
                return -1000


    #two-side-open-3-in-a-row for me
    #horizontal
    for i in range(0,5):
        for j in range(1,3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == me and board[i][j-1] == board[i][j+3] == "N":
                heur += 200

    #vertical
    i = 1
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == me and board[i-1][j] == board[i+3][j] == "N":
            heur += 200

    #diagonal
    i = 1
    for j in range(1,3):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == me and board[i-1][j-1] == board[i+3][j+3] == "N":
            heur += 200
    
    i = 3
    for j in range(1,3):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == me and board[i+1][j-1] == board[i-3][j+3] == "N":
            heur += 200

    #two-side-open-3-in-a-row for opponent
    #horizontal
    for i in range(0,5):
        for j in range(1,3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == opponent and board[i][j-1] == board[i][j+3] == "N":
                heur -= 80

    #vertical
    i = 1
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == opponent and board[i-1][j] == board[i+3][j] == "N":
            heur -= 80

    #diagonal
    i = 1
    for j in range(1,3):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == opponent and board[i-1][j-1] == board[i+3][j+3] == "N":
            heur -= 80
    
    i = 3
    for j in range(1,3):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == opponent and board[i+1][j-1] == board[i-3][j+3] == "N":
            heur -= 80

    #one-side-open-3-in-a-row for me
    #horizontal
    for i in range(0,5):
        for j in range(1,3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == me and ((board[i][j-1] == "N" and board[i][j+3] == opponent) or (board[i][j-1] == opponent and board[i][j+3] == "N")):
                heur += 150

    j = 0
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == board[i][j+2] == me and board[i][j+3] == "N":
            heur += 150

    j = 3
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == board[i][j+2] == me and board[i][j-1] == "N":
            heur += 150

    #vertical
    i = 1
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == me and ((board[i-1][j] == "N" and board[i+3][j] == opponent) or (board[i-1][j] == opponent and board[i+3][j] == "N")):
            heur += 150

    i = 0
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == me and board[i+3][j] == "N":
            heur += 150
    
    i = 2
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == me and board[i-1][j] == "N":
            heur += 150

    #diagonal
    i = 1
    for j in range(1,3):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == me and ((board[i-1][j-1] == "N" and board[i+3][j+3] == opponent) or (board[i-1][j-1] == opponent and board[i+3][j+3] == "N")):
            heur += 150
    
    i = 0
    for j in range(0,3):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == me and board[i+3][j+3] == "N":
            heur += 150
    
    i = 1
    j = 0
    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == me and board[i+3][j+3] == "N":
        heur += 150

    i = 1
    j = 3
    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == me and board[i-1][j-1] == "N":
        heur += 150

    i = 2
    for j in range(1,4):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == me and board[i-1][j-1] == "N":
            heur += 150

    i = 3
    for j in range(1,3):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == me and ((board[i+1][j-1] == "N" and board[i-3][j+3] == opponent) or (board[i+1][j-1] == opponent and board[i-3][j+3] == "N")):
            heur += 150

    i = 2
    for j in range(1,4):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == me and board[i+1][j-1] == "N":
            heur += 150

    i = 3
    j = 0
    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == me and board[i-3][j+3] == "N":
        heur += 150

    i = 3
    j = 3
    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == me and board[i+1][j-1] == "N":
        heur += 150
    
    i = 4
    for j in range(0,3):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == me and board[i-3][j+3] == "N":
            heur += 150

    #one-side-open-3-in-a-row for opponent
    #horizontal
    for i in range(0,5):
        for j in range(1,3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == opponent and ((board[i][j-1] == "N" and board[i][j+3] == me) or (board[i][j-1] == me and board[i][j+3] == "N")):
                heur -= 40

    j = 0
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == board[i][j+2] == opponent and board[i][j+3] == "N":
            heur -= 40

    j = 3
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == board[i][j+2] == opponent and board[i][j-1] == "N":
            heur -= 40

    #vertical
    i = 1
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == opponent and ((board[i-1][j] == "N" and board[i+3][j] == me) or (board[i-1][j] == me and board[i+3][j] == "N")):
            heur -= 40

    i = 0
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == opponent and board[i+3][j] == "N":
            heur -= 40
    
    i = 2
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == board[i+2][j] == opponent and board[i-1][j] == "N":
            heur -= 40

    #diagonal
    i = 1
    for j in range(1,3):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == opponent and ((board[i-1][j-1] == "N" and board[i+3][j+3] == me) or (board[i-1][j-1] == me and board[i+3][j+3] == "N")):
            heur -= 40
    
    i = 0
    for j in range(0,3):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == opponent and board[i+3][j+3] == "N":
            heur -= 40
    
    i = 1
    j = 0
    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == opponent and board[i+3][j+3] == "N":
        heur -= 40

    i = 1
    j = 3
    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == opponent and board[i-1][j-1] == "N":
        heur -= 40

    i = 2
    for j in range(1,4):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == opponent and board[i-1][j-1] == "N":
            heur -= 40

    i = 3
    for j in range(1,3):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == opponent and ((board[i+1][j-1] == "N" and board[i-3][j+3] == me) or (board[i+1][j-1] == me and board[i-3][j+3] == "N")):
            heur -= 40

    i = 2
    for j in range(1,4):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == opponent and board[i+1][j-1] == "N":
            heur -= 40

    i = 3
    j = 0
    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == opponent and board[i-3][j+3] == "N":
        heur -= 40

    i = 3
    j = 3
    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == opponent and board[i+1][j-1] == "N":
        heur -= 40
    
    i = 4
    for j in range(0,3):
        if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == opponent and board[i-3][j+3] == "N":
            heur -= 40

    #two-side-open-2-in-a-row for me
    #horizontal
    for i in range(0,5):
        for j in range(1,4):
            if board[i][j] == board[i][j+1] == me and board[i][j-1] == board[i][j+2] == "N":
                heur += 20

    #vertical
    for i in range(1,3):
        for j in range(0,6):
            if board[i][j] == board[i+1][j] == me and board[i-1][j] == board[i+2][j] == "N":
                heur += 20

    #diagonal
    for i in range(1,3):
        for j in range(1,4):
            if board[i][j] == board[i+1][j+1] == me and board[i-1][j-1] == board[i+2][j+2] == "N":
                heur += 20
    
    for i in range(2,4):
        for j in range(1,4):
            if board[i][j] == board[i-1][j+1] == me and board[i+1][j-1] == board[i-2][j+2] == "N":
                heur += 20

    #two-side-open-2-in-a-row for opponent
    #horizontal
    for i in range(0,5):
        for j in range(1,4):
            if board[i][j] == board[i][j+1] == opponent and board[i][j-1] == board[i][j+2] == "N":
                heur -= 15

    #vertical
    for i in range(1,3):
        for j in range(0,6):
            if board[i][j] == board[i+1][j] == opponent and board[i-1][j] == board[i+2][j] == "N":
                heur -= 15

    #diagonal
    for i in range(1,3):
        for j in range(1,4):
            if board[i][j] == board[i+1][j+1] == opponent and board[i-1][j-1] == board[i+2][j+2] == "N":
                heur -= 15
    
    for i in range(2,4):
        for j in range(1,4):
            if board[i][j] == board[i-1][j+1] == opponent and board[i+1][j-1] == board[i-2][j+2] == "N":
                heur -= 15

    #one-side-open-2-in-a-row for me
    #horizontal
    for i in range(0,5):
        for j in range(1,4):
            if board[i][j] == board[i][j+1] == me and ((board[i][j-1] == "N" and board[i][j+2] == opponent) or (board[i][j-1] == opponent and board[i][j+2] == "N")):
                heur += 5

    j = 0
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == me and board[i][j+2] == "N":
            heur += 5

    j = 4
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == me and board[i][j-1] == "N":
            heur += 5

    #vertical
    for i in range(1,3):
        for j in range(0,6):
            if board[i][j] == board[i+1][j] == me and ((board[i-1][j] == "N" and board[i+2][j] == opponent) or (board[i-1][j] == opponent and board[i+2][j] == "N")):
                heur += 5

    i = 0
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == me and board[i+2][j] == "N":
            heur += 5
    
    i = 3
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == me and board[i-1][j] == "N":
            heur += 5

    #diagonal
    for i in range(1,3):
        for j in range(1,4):
            if board[i][j] == board[i+1][j+1] == me and ((board[i-1][j-1] == "N" and board[i+2][j+2] == opponent) or (board[i-1][j-1] == opponent and board[i+2][j+2] == "N")):
                heur += 5
    
    i = 0
    for j in range(0,4):
        if board[i][j] == board[i+1][j+1] == me and board[i+2][j+2] == "N":
            heur += 5
    
    j = 0
    for i in range(1,3):
        if board[i][j] == board[i+1][j+1] == me and board[i+2][j+2] == "N":
            heur += 5

    j = 4
    for i in range(1,3):
        if board[i][j] == board[i+1][j+1] == me and board[i-1][j-1] == "N":
            heur += 5

    i = 3
    for j in range(1,5):
        if board[i][j] == board[i+1][j+1] == me and board[i-1][j-1] == "N":
            heur += 5

    for i in range(2,4):
        for j in range(1,4):
            if board[i][j] == board[i-1][j+1] == me and ((board[i+1][j-1] == "N" and board[i-2][j+2] == opponent) or (board[i+1][j-1] == opponent and board[i-2][j+2] == "N")):
                heur += 5

    i = 1
    for j in range(1,5):
        if board[i][j] == board[i-1][j+1] == me and board[i+1][j-1] == "N":
            heur += 5

    j = 0
    for i in range(2,4):
        if board[i][j] == board[i-1][j+1] == me and board[i-2][j+2] == "N":
            heur += 5

    j = 4
    for i in range(2,4):
        if board[i][j] == board[i-1][j+1] == me and board[i+1][j-1] == "N":
            heur += 5
    
    i = 4
    for j in range(0,4):
        if board[i][j] == board[i-1][j+1] == me and board[i-2][j+2] == "N":
            heur += 5

    #one-side-open-2-in-a-row for opponent
    #horizontal
    for i in range(0,5):
        for j in range(1,4):
            if board[i][j] == board[i][j+1] == opponent and ((board[i][j-1] == "N" and board[i][j+2] == me) or (board[i][j-1] == me and board[i][j+2] == "N")):
                heur -= 2

    j = 0
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == opponent and board[i][j+2] == "N":
            heur -= 2

    j = 4
    for i in range(0,5):
        if board[i][j] == board[i][j+1] == opponent and board[i][j-1] == "N":
            heur -= 2

    #vertical
    for i in range(1,3):
        for j in range(0,6):
            if board[i][j] == board[i+1][j] == opponent and ((board[i-1][j] == "N" and board[i+2][j] == me) or (board[i-1][j] == me and board[i+2][j] == "N")):
                heur -= 2

    i = 0
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == opponent and board[i+2][j] == "N":
            heur -= 2
    
    i = 3
    for j in range(0,6):
        if board[i][j] == board[i+1][j] == opponent and board[i-1][j] == "N":
            heur -= 2

    #diagonal
    for i in range(1,3):
        for j in range(1,4):
            if board[i][j] == board[i+1][j+1] == opponent and ((board[i-1][j-1] == "N" and board[i+2][j+2] == me) or (board[i-1][j-1] == me and board[i+2][j+2] == "N")):
                heur -= 2
    
    i = 0
    for j in range(0,4):
        if board[i][j] == board[i+1][j+1] == opponent and board[i+2][j+2] == "N":
            heur -= 2
    
    j = 0
    for i in range(1,3):
        if board[i][j] == board[i+1][j+1] == opponent and board[i+2][j+2] == "N":
            heur -= 2

    j = 4
    for i in range(1,3):
        if board[i][j] == board[i+1][j+1] == opponent and board[i-1][j-1] == "N":
            heur -= 2

    i = 3
    for j in range(1,5):
        if board[i][j] == board[i+1][j+1] == opponent and board[i-1][j-1] == "N":
            heur -= 2

    for i in range(2,4):
        for j in range(1,4):
            if board[i][j] == board[i-1][j+1] == opponent and ((board[i+1][j-1] == "N" and board[i-2][j+2] == me) or (board[i+1][j-1] == me and board[i-2][j+2] == "N")):
                heur -= 2

    i = 1
    for j in range(1,5):
        if board[i][j] == board[i-1][j+1] == opponent and board[i+1][j-1] == "N":
            heur -= 2

    j = 0
    for i in range(2,4):
        if board[i][j] == board[i-1][j+1] == opponent and board[i-2][j+2] == "N":
            heur -= 2

    j = 4
    for i in range(2,4):
        if board[i][j] == board[i-1][j+1] == opponent and board[i+1][j-1] == "N":
            heur -= 2
    
    i = 4
    for j in range(0,4):
        if board[i][j] == board[i-1][j+1] == opponent and board[i-2][j+2] == "N":
            heur -= 2

    return heur

def legal_moves(board,player):
    legal_moves = []
    
    for j in range(0,6):
        for i in range(0,5):
            if board[i][j] == "N":
                flag = 0
                if i-1 >= 0 and j-1 >= 0:
                    if board[i-1][j-1] != "N":
                        flag = 1
                if i-1 >= 0:
                    if board[i-1][j] != "N":
                        flag = 1
                if i-1 >= 0 and j+1 <= 5:
                    if board[i-1][j+1] != "N":
                        flag = 1
                if j-1 >= 0:
                    if board[i][j-1] != "N":
                        flag = 1
                if j+1 <= 5:
                    if board[i][j+1] != "N":
                        flag = 1
                if i+1 <= 4 and j-1 >= 0:
                    if board[i+1][j-1] != "N":
                        flag = 1
                if i+1 <= 4:
                    if board[i+1][j] != "N":
                        flag = 1
                if i+1 <= 4 and j+1 <= 5:
                    if board[i+1][j+1] != "N":
                        flag = 1
                if flag == 1:
                    board_child = copy.deepcopy(board)
                    board_child[i][j] = player
                    legal_moves.append(([i,j],heuristic(board_child,player)))
 
    return legal_moves

def find_terminalNodes(board, player):
    condition = len(legal_moves(board,player)) == 0
    if(condition):
        return True

def place_piece(board, player, position):
    copyBoard = copy.deepcopy(board)
    print(position)
    copyBoard[position[0]][position[1]] = player

    for r in copyBoard:
        for c in r:
            print(c,end = " ")
        print()
    return copyBoard

def minimax2ply(board, player, depth, max_min_player):
    copyBoard = copy.deepcopy(board)
    terminal_found = find_terminalNodes(board,player)
    list_moves =  legal_moves(board,player)
    totalNodes = 0
    
    #Terminal node is when player X or O wins, or the board is full
    if depth == 0 or terminal_found:
        if terminal_found == True:
            print("Game is Over")
        elif(heuristic(board, player) == 1000 or heuristic(board, player) == -1000):
            return 10000
        # The depth is 0, return the evaluation of the node
        else:
            return heuristic(board, player)

    if max_min_player:
        score = -math.inf
        new_score = 0
        maxNum = 0
        position = []

        for moves in (list_moves):
            print(moves[1])
            if(moves[1] > maxNum):
                maxNum = moves[1]
                position = moves[0]
                print(position)
        newBoard = place_piece(copyBoard,player,position)
        # Set to false to switch to min
        new_score = max(maxNum, minimax2ply(newBoard,player, depth-1, False))
        print(maxNum, " is the max", position)
        return new_score

    # Min player
    else:
        score = -math.inf
        new_score = 0
        minNum = math.inf
        position = []

        for moves in (list_moves):
            # print(moves[1])
            if(moves[1] < minNum):
                minNum = moves[1]
                position = moves[0]
                
        newBoard2 = place_piece(copyBoard,player,position)
        # Set to True to switch to max
        new_score = min(minNum, minimax2ply(newBoard2,player, depth-1, True))
        return new_score

def minimax4ply(board, player, depth, max_min_player):
    copyBoard = copy.deepcopy(board)
    terminal_found = find_terminalNodes(board,player)
    list_moves =  legal_moves(board,player)
    totalNodes = 0
    
    #Terminal node is when player X or O wins, or the board is full
    if depth == 0 or terminal_found:
        if terminal_found == True:
            print("Game is Over")
        # The depth is 0, return the evaluation of the node
        else:
            return heuristic(board, player)

    if max_min_player:
        score = -math.inf
        new_score = 0
        # For each move we can take
        maxNum = 0
        position = []

        for moves in (list_moves):
            print(moves[1])
            if(moves[1] > maxNum):
                maxNum = moves[1]
                position = moves[0]

        newBoard = place_piece(copyBoard,player,position)
        # Set to false to switch to min
        new_score = max(minimax2ply(newBoard,player, depth-1, False))
        print(maxNum, " is the max", position)
        return new_score

    # Min player
    else:
        score = -math.inf
        new_score = 0
        # For each move we can take
        minNum = math.inf
        position = []

        for moves in (list_moves):
            print(moves[1])
            if(moves[1] < minNum):
                minNum = moves[1]
                position = moves[0]
                
        newBoard2 = place_piece(copyBoard,player,position)
        # Set to false to switch to min
        new_score = min(minimax2ply(newBoard2,player, depth-1, False))
        return new_score

if __name__ == "__main__":
    # N is for None, no x or o place on that location
    board = [
        ["N","N","N","N","N","N"],
        ["N","N","N","N","N","N"],
        ["N","N","N","N","N","N"],
        ["N","N","N","N","N","N"],
        ["N","N","N","N","N","N"]]

    
    board1 = [
        ["N","N","N","N","N","N"],
        ["N","N","O","X","N","N"],
        ["N","N","O","O","X","N"],
        ["N","O","X","X","O","N"],
        ["N","N","X","N","N","N"]]
    

    # Start player 1 at 3,4
    board[2][3] = "X"
    print()

    for r in board:
        for c in r:
            print(c,end = " ")
        print()

    print(heuristic(board1,"X"))

    print(legal_moves(board1,"X"))

    winner = False
    playerTurn = 'X'
    start = time.time()
    findWinner = ""
    # testing
    minimax2ply(board1,playerTurn,2,True)
    # while not winner:
    #     if(playerTurn == 'p2'):
    #       playerTurn = 'p1'
    #       move = minimax2ply(board1,playerTurn,2,True)
    #       win = heuristic(board, playerTurn)
    #       if(win == 1000):
    #           winner = True
    #           findWinner = "player 2"
    #     else:
    #       playerTurn = 'p2' 
    #       move = minimax2ply(board1,playerTurn,2,True)
    #       win = heuristic(board, playerTurn)
    #       if(win == 1000):
    #           winner = True
    #           findWinner = "player 1"

    end = time.time()
    totalTime = end - start
    print(totalTime)
