import sys
from ConnectNGame.src import game
def main() -> None:
    startgame = game.Game(sys.argv[1])  # program execution begins here
    startgame.game()

if __name__ == '__main__':
    main()
