def printBoard(b):
    print(f"{b["7"]} | {b["8"]} | {b["9"]}\n-+-+-")
    print(f"{b["4"]} | {b["5"]} | {b["6"]}\n-+-+-")
    print(f"{b["1"]} | {b["2"]} | {b["3"]}\n-+-+-")
def checkwin(b, t):
     win_patterns=[("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"), ("1", "4", "7"), ("2", "5", "8"), ("3", "6", "9"), ("1", "5", "9"), ("3", "5", "7")]
     return any(b[x]==b[y]==b[z]==t for x, y, z in win_patterns)
def game():
    board={str(i): ' ' for i in range(1, 10)}
    turn='X'
    for move_count in range(9):
        printBoard(board)
        move=input(f"Player {turn}, enter your move (1-9): ")
        if board.get(move) != ' ':
             print("Invalid move, try again.")
             continue
        board[move]=turn
        if move_count >= 4 and checkwin(board, turn):
             printBoard(board)
             print(f"Player {turn} wins!")
             break
        turn='O' if turn=='X' else 'X'
    else:     
        printBoard(board)
        print("It's a draw!")                       
    if input("Play again? (y/n): ").lower() == 'y':
     game()
if __name__ == "__main__":
    game()
        

   
