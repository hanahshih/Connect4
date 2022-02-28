import string
class Player(object):
    while True:
        p1 = input('Player 1 enter your name:')

        def has_whitespace(self: str):
            return True in [i in self for i in string.whitespace]

        if has_whitespace(p1) == True:
            print('Your name cannot be the empty string or whitespace')
            continue
        elif p1 == '':
            print("Your name cannot be the empty string or whitespace")
            continue
        else:
            break
    while True:
        p1_piece = input('Player 1 enter your piece:')
        if has_whitespace(p1_piece) == True:
            print('Your piece cannot be the empty string or whitespace')
            continue
        elif p1_piece == '':
            print('Your piece cannot be the empty string or whitespace')
            continue
        elif len(p1_piece) > 1:
            print(p1_piece + ' is not a single character. Your piece can only be a single character.')
            continue
        elif p1_piece == '*':
            print('Your piece cannot be the same as the blank character.')
            continue
        else:
            break
    while True:
        p2 = input("Player 2 enter your name:")

        def not_the_same(p1, p2):
            p1 = p1.upper()
            p2 = p2.upper()
            if p1 == p2:
                return True

        if has_whitespace(p2) == True:
            print('Your name cannot be the empty string or whitespace')
            continue
        elif p2 == '':
            print('Your name cannot be the empty string or whitespace')
            continue
        elif not_the_same(p1, p2) == True:
            print('You cannot use ' + p2 + ' for your name as someone else is already using it')
            continue
        else:
            break
    while True:
        p2_piece = input('Player 2 enter your piece:')

        def not_the_same(p1, p2):
            p1 = p1.upper()
            p2 = p2.upper()
            if p1 == p2:
                return True

        if has_whitespace(p2_piece) == True:
            print('Your piece cannot be the empty string or whitespace')
            continue
        elif p2_piece == '':
            print('Your piece cannot be the empty string or whitespace')
            continue
        elif not_the_same(p1_piece, p2_piece) == True:
            print('You cannot use ' + p2_piece + ' for your piece as ' + p1 + ' is already using it')
            continue
        elif len(p2_piece) > 1:
            print(p2_piece + ' is not a single character. Your piece can only be a single character.')
            continue
        elif p2_piece == '*':
            print('Your piece cannot be the same as the blank character.')
            continue
        else:
            break
