

def horizontal_Check():
    None

def vertical_Check():
    None

def diagonal_Check():
    None

def heuristic():
    None

def minimax2ply():
    None

def minimax4ply():
    None

if __name__ == "__main__":
    # N is for None, no x or o place on that location
    map = [[
        "N","N","N","N","N","N"],
        ["N","N","N","N","N","N"],
        ["N","N","N","N","N","N"],
        ["N","N","N","N","N","N"],
        ["N","N","N","N","N","N"]]

    # Start player 1 at 3,4
    map[2][3] = "X"
    print()

    for r in map:
        for c in r:
            print(c,end = " ")
        print()


