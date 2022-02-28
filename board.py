#!/usr/bin/env python
# coding: utf-8

# In[36]:

class Board(object):

    def create(row, col):
        # create a board
        row = int(row)
        col = int(col)
        board=[['*'] * col for i in range(row)]
        return board



    def show_board(row, col):
        for i in range(col):
            print("  ", str(i), end=" ")
        print(" ")
        row_count = 0
        for i in row:
            print(str(row_count), str(i))
            row_count+=1



    # In[50]:


    def move(state, choice, piece):
        # find lowest open spot in choice row to put piece
        for i in range(len(state) - 1, -1, -1):
            if state[i][choice] == "*":
                state[i][choice] = piece
                return


    # In[4]:


    def valid(state, choice):
        if state[0][choice] == "*":
            return True
        else:
            return False


    # In[5]:


    def check_above(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.board.check_above(state, row - 1, col, total + 1, piece)
        else:
            return total


    def check_below(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.check_below(state, row + 1, col, total + 1, piece)
        else:
            return total


    def check_left(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.check_left(state, row, col - 1, total + 1, piece)
        else:
            return total


    def check_right(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.check_right(state, row, col + 1, total + 1, piece)
        else:
            return total


    def check_right_diag_up(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.check_right_diag_up(state, row - 1, col + 1, total + 1, piece)
        else:
            return total


    def check_right_diag_down(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.check_right_diag_down(state, row + 1, col - 1, total + 1, piece)
        else:
            return total


    def check_left_diag_up(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.check_left_diag_up(state, row - 1, col - 1, total + 1, piece)
        else:
            return total


    def check_left_diag_down(state, row, col, total, piece):
        if row < 0 or row >= len(state) or col < 0 or col >= len(state[0]):
            return total
        if state[row][col] == piece:
            return Board.check_left_diag_down(state, row + 1, col + 1, total + 1, piece)
        else:
            return total


    # In[39]:


    def check_win(state, col, piece):
        # we find if we have won by looking at the most recent placement and checking above, below, left and right
        # and both diagnols
        row = -1
        #print(piece)
        for i in range(len(state)):
            if state[i][col] == piece:
                row = i
                break
        #print(state[row][col])
        num_top = Board.check_above(state, row - 1, col, 0, piece)
        num_below = Board.check_below(state, row + 1, col, 0, piece)
        if num_top + num_below + 1 >= 4:
            return True
        num_left = Board.check_left(state, row, col - 1, 0, piece)
        num_right = Board.check_right(state, row, col + 1, 0, piece)
        if num_left + num_right + 1 >= 4:
            return True
        num_right_diag_up = Board.check_right_diag_up(state, row - 1, col + 1, 0, piece)
        num_right_diag_down = Board.check_right_diag_down(state, row + 1, col - 1, 0, piece)
        if num_right_diag_up + num_right_diag_down + 1 >= 4:
            return True
        num_left_diag_up = Board.check_left_diag_up(state, row - 1, col - 1, 0, piece)
        num_left_diag_down = Board.check_left_diag_down(state, row + 1, col + 1, 0, piece)
        if num_left_diag_up + num_left_diag_down + 1 >= 4:
            return True
        return False


    def check_tie(state):
        # check to see if the board is full
        for i in state[0]:
            if i == "*":
                return False
        return True


# In[51]:



