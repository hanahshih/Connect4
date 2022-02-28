import string
from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player
class Game(object):
    def game():

        row = int(input('rows:'))
        column = int(input('columns:'))
        board = Board.create(row, column)
        curr = 1
        currpiece = Player.p1_piece
        while True:
            Board.show_board(board, column)
            if curr == 1:
                current_player = Player.p1
            elif curr == 2:
                current_player = Player.p2
            col = int(input(current_player + " , please enter the column you want to play in "))

            if Board.check_tie(board):
                print("Game is tied!")
                break
            else:
                if Board.valid(board, col-1):
                    Board.move(board, col, currpiece)
                    if Board.check_win(board, col, currpiece):
                        Board.show_board(board, column)
                        print(current_player + " has won the game!")
                        break
                    else:
                        if curr == 1:
                            curr = 2
                            current_player = Player.p2
                            currpiece = Player.p2_piece
                        else:
                            curr = 1
                            current_player = Player.p1
                            currpiece = Player.p1_piece

                else:
                    print("That is not a valid move. Please try again")

    game()
