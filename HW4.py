def heuristic(board,player):
    heur = 0
    if player == "X":
        me = "X"
        opponent = "O"
    else:
        me = "O"
        opponent = "X"

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

def minimax2ply():
    None

def minimax4ply():
    None

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