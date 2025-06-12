d=[1,2,3],[4,5,6],[7,8,9]
def structure():
    for i in range(3):
        for j in range(1):
            print(f"| {d[i][j]} | {d[i][j+1]} | {d[i][j+2]} |")
        if i<2:
            print("|---|---|---|")
    print("\n")
structure()

def inp1():
    p1 = int(input("Player 1:- "))
    if p1>0 and p1<4:
        if d[0][p1-1]=='X':
            print("Position already taken by you.\nTRY AGAIN!")
            structure()
            inp1()
        elif d[0][p1-1]=='O':
            print("Position already taken by Opponent.\nTRY AGAIN!")
            structure()
            inp1()
    elif p1>3 and p1<7:
        if d[1][p1-4]=='X':
            print("Position already taken by you.\nTRY AGAIN!")
            structure()
            inp1()
        elif d[1][p1-4]=='O':
            print("Position already taken by Opponent.\nTRY AGAIN!")
            structure()
            inp1()
    elif p1>6 and p1<10:
        if d[2][p1-7]=='X':
            print("Position already taken by you.\nTRY AGAIN!")
            structure()
            inp1()
        elif d[2][p1-7]=='O':
            print("Position already taken by Opponent.\nTRY AGAIN!")
            structure()
            inp1()
    else:
        print("This position is not valid.\nTRY AGAIN!")
        structure()
        inp1()

    for i in range(3):
        for j in range(3):
            if p1==d[i][j]:
                d[i][j]="X"
                structure()
def inp2():
    p2 = int(input("Player 2:- "))
    if p2>0 and p2<4:
        if d[0][p2-1]=='O':
            print("Position already taken by you.\nTRY AGAIN!")
            structure()
            inp2()
        elif d[0][p2-1]=='X':
            print("Position already taken by Opponent.\nTRY AGAIN!")
            structure()
            inp2()
    elif p2>3 and p2<7:
        if d[1][p2-4]=='O':
            print("Position already taken by you.\nTRY AGAIN!")
            structure()
            inp2()
        elif d[1][p2-4]=='X':
            print("Position already taken by Opponent.\nTRY AGAIN!")
            structure()
            inp2()
    elif p2>6 and p2<10:
        if d[2][p2-7]=='O':
            print("Position already taken by you.\nTRY AGAIN!")
            structure()
            inp2()
        elif d[2][p2-7]=='X':
            print("Position already taken by Opponent.\nTRY AGAIN!")
            structure()
            inp2()
    else:
        print("This position is not valid.\nTRY AGAIN!")
        structure()
        inp2()
    for i in range(3):
        for j in range(3):
            if p2==d[i][j]:
                d[i][j]="O"
                structure()

def horizontal_check():
    for i in range(3):
        for j in range(1):
            if d[i][j]==d[i][j+1]==d[i][j+2]=="O":
                print("Player 2 WON")
                exit(0)
            elif d[i][j]==d[i][j+1]==d[i][j+2]=="X":
                print("Player 1 WON")
                exit(0)
            else:
                continue
def vertical_check():
    for i in range(1):
        for j in range(3):
            if d[i][j]==d[i+1][j]==d[i+2][j]=="O":
                print("Player 2 WON")
                exit(0)
            elif d[i][j]==d[i+1][j]==d[i+2][j]=="X":
                print("Player 1 WON")
                exit(0)
            else:
                continue
def diagonal_check():
    if d[0][0]==d[1][1]==d[2][2]=="O":
        print("Player 2 WON")
        exit(0)
    elif d[0][2]==d[1][1]==d[2][0]=="O":
        print("Player 2 WON")
        exit(0)
    elif d[0][0]==d[1][1]==d[2][2]=="X":
        print("Player 1 WON")
        exit(0)
    elif d[0][2]==d[1][1]==d[2][0]=="X":
        print("Player 1 WON")
        exit(0)
def draw_check():
    c = 0
    for i in range(3):
        for j in range(3):
            if d[i][j]=="O" or d[i][j]=="X":
                c+=1
            else:
                pass
    if c == 9:
        print("Game Draw!!!!!!!!!!!!!!!!!!!")
        exit(0)
    
def execute():
    random = 0
    while random==0:
        inp1()
        horizontal_check()
        vertical_check()
        diagonal_check()
        draw_check()
        inp2()
        horizontal_check()
        vertical_check()
        diagonal_check()
        draw_check()
execute()