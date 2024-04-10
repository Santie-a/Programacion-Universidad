def create_board():
    return [" "] * 9

def select_characters():
    while True:
        inp = input("Select 'x' or 'o': ").lower()
        if inp == "x":
            return "x", "o"
        if inp == "o":
            return "o", "x"
        print("Los datos ingresados no son válidos!")
        
def print_board(board):
    for i, el in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("\n---------------")
        print(f"| {el} ", end="|")
    print()
        
def update_board(board, character, is_computer=False):
    if not is_computer:
        while True:
            try:
                inp = int(input("Ingrese la posición donde quiere realizar su jugada (1 - 9): ")) - 1
                if inp >= 0 and inp <= 8 and board[inp] == " ":
                    board[inp] = character
                    break
            except:
                print("La posicón introducida no es válida!")
    else:
        opp = "x" if character == "o" else "o"
        for i in range(len(board)):
            board_copy = board[:]
            board_copy[i] = character if board_copy[i] == " " else board_copy[i]
            if is_winner(board_copy):
                board[i] = character
                return
                
        for i in range(len(board)):
            board_copy = board[:]
            board_copy[i] = opp if board_copy[i] == " " else board_copy[i]
            if is_winner(board_copy):
                board[i] = character
                return
            
        for i in [0, 2, 6, 8]:
            if board[i] == " ":
                board[i] = character
                return
            
        if board[i] == " ":
            board[i] = character
            return
            
        for i in [1, 3, 5, 7]:
            if board[i] == " ":
                board[i] = character
                return
            
def is_winner(board):
    if (board[0] == 'x' and board[1] == 'x' and board[2] == 'x') or (board[3] == 'x' and board[4] == 'x' and board[5] == 'x') or (board[6] == 'x' and board[7] == 'x' and board[8] == 'x') or (board[0] == 'x' and board[4] == 'x' and board[8] == 'x') or (board[2] == 'x' and board[4] == 'x' and board[6] == 'x') or (board[0] == 'x' and board[3] == 'x' and board[6] == 'x') or (board[1] == 'x' and board[4] == 'x' and board[7] == 'x') or (board[2] == 'x' and board[5] == 'x' and board[8] == 'x'):
        return True, "x"
    
    if (board[0] == 'o' and board[1] == 'o' and board[2] == 'o') or (board[3] == 'o' and board[4] == 'o' and board[5] == 'o') or (board[6] == 'o' and board[7] == 'o' and board[8] == 'o') or (board[0] == 'o' and board[4] == 'o' and board[8] == 'o') or (board[2] == 'o' and board[4] == 'o' and board[6] == 'o') or (board[0] == 'o' and board[3] == 'o' and board[6] == 'o') or (board[1] == 'o' and board[4] == 'o' and board[7] == 'o') or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o'):
        return True, "o"
    
    return False
                
def main():
    board = create_board()
    user, computer = select_characters()
    turn = 0 if user == "x" else 1
    while not is_winner(board):
        if not turn:
            print("Turno del jugador.")
            update_board(board, user)
            turn = 1
        else:
            print("Turno de la computadora.")
            update_board(board, computer, is_computer=True)
            turn = 0
        
        print_board(board)
        
        if not " " in board:
            print("Draw")
            if input("Quieres jugar otra vez?: s/n: ").lower().startswith("n"):
                return
            main()

    winner, winner_char = is_winner(board)
    if winner:
        print(f"Ganan las {winner_char}'s")
        if input("Quieres jugar otra vez?: s/n: ").lower().startswith("n"):
            return
        main()
            
if __name__ == "__main__":
    main()