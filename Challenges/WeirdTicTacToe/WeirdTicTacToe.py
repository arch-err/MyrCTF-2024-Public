"""
This program lets you play tic-tac-toe but it also does something a bit strange...

It can be quite dificult to find what is hidden so I'll give you FLAG (futher down) for free,
and even though it might be tempting to just past it into the code somewhere and call it a day,
I think you will want to play your way through the game.
Nontheless, I encurage you to use FLAG in the code scince it might give you,
hmm... well, a picture of where you're going so to speak.

FLAG = ['293031323334352828', '198201204205206169169169169', '141414161417141814191421121512151215', '141661416714168141691417014171141721417314174']
"""

from Board import *

def Main():
    board = Board()
    while not board.win:
        board.PrintBoard()
        board.PlacePiece(int(input()))
        board.CheckWin()

if __name__ == "__main__":
    Main()