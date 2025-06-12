def print_board(board):
    for i in range(3):
        print("|".join(board[i]))
        if i<2:
            print("-----")
            
def check_winner(board):
    for row in board:
        if row[0]==row[1]==row[2]!='':
            return True
        
    for col in range (3):
        if board[0][col]==board[1][col]==board[2][col]!='':
            return True
        
    if board[0][0]==board[1][1]==board[2][2]!='':
        return True
    if board[0][2]==board[1][1]==board[2][0]!='':
        return True


    return False

def is_board_full(board):
    for row in board:
        if '' in row:
            return False
    return True

def main():
    board=[[''for _ in range(3)]for _ in range(3)]
    current_player='X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row=int(input("Enter row (0-2):"))
            col=int(input("Enter column (0-2):"))

            if row<0 or row>2 or col<0 or col>2:
                print("Invalid position")
                continue

            board[row][col]=current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            elif is_board_full(board):
                print_board(board)
                print("IT's a tie!")
                break

            current_player='O' if current_player=='X' else 'X'

        except ValueError:
            print("Invalid input, enter integers between 0 and 2.")

if __name__=="__main__":
    main()

    
