from EndGame import *

class Board(object):
    def __init__(self):
        """
        spaces:     dictionary containing the 9 spaces on the board, a space can have the value 'O', 'X' or False
        current:    used as index (0 or -1) when placing a piece, used as a bolean value when switching whose turn it is
        lastPlaced: keeps track of the last placed piece in order to alow a player to change their mind
        win:        True when a player has won or when 4 rounds have been played (is set to False after a win has been declared if it's not the 4th round)
        history:    a string of numbers is added after compleatng a round, the string is created based on the end-state of the board
        valus:      values for every space in spaces, used to calculate history
        """
        self.spaces = {n:False for n in range(9)}
        self.pieces = ('O','X')
        self.current = False
        self.lastPlaced = None
        self.win = False
        self.history = []
        self.values = [n for n in range(1,10)]

        global winScenarios
        winScenarios = ('012','345','678','036','147','258','048','246')
    
    def PrintBoard(self):
        """
        Prints the board and the currently placed pieces
        """
        pBoard = [self.spaces[n] if self.spaces[n] else ' ' for n in range(9)]
        print(' %s | %s | %s \n-----------' % (pBoard[0], pBoard[1], pBoard[2]))
        print(' %s | %s | %s \n-----------' % (pBoard[3], pBoard[4], pBoard[5]))
        print(' %s | %s | %s ' % (pBoard[6], pBoard[7], pBoard[8]))

    def ClearBoard(self):
        """
        Clears the board by setting the value of every element in spaces to False
        """
        for n in range(9):
            self.spaces[n] = False

    def PlacePiece(self,space):
        """
        Places a piece in space
        Removes a piece if space is occupied by the last placed piece
        """
        if not self.spaces[space] or space == self.lastPlaced:
            if self.spaces[space]:
                self.spaces[space] = False
                self.current = False if self.current else True
            else:
                self.spaces[space] = self.pieces[self.current]
                self.current = False if self.current else True
                self.lastPlaced = space

    def CheckWin(self):
        """
        Checks if the board contains one of the winScenarios and if that's the case, sets win = True and calls Restart
        If every space on the board contains a piece, Restart is also called
        """
        for s in winScenarios:
            if self.spaces[int(s[0])] and self.spaces[int(s[0])] == self.spaces[int(s[1])] and self.spaces[int(s[1])] == self.spaces[int(s[2])]:
                self.win = True
                self.Restart(s)
        full = True
        for s in range(9):
            full = full and self.spaces[s]
        if full:
            self.Restart(s)

    def Restart(self,winscenario):
        """
        Restart contains three parts, it calls CalcHistory and, if win == True, ShowWin
        Finaly, it checks how many rounds have been played and calls EndOfGame if the 4th round has been played
        """
        self.CalcHistory()

        if self.win:
            self.ShowWin(winscenario)
        else:
            self.PrintBoard()

        # If this is the end of the 4th round, go to EndOfGame, else: restart after the user has pushed ENTER
        if len(self.history) == 4:
            self.EndOfGame()
            self.win = True
        else:
            self.win = False
            self.ClearBoard()
            self.lastPlaced = None
            input()
    
    def CalcHistory(self):
        """
        Calculates the string of numbers for this round which is stored in history
        """
        historyLen = {0:18, 1:27, 2:36, 3:45}
        tempHistory = ''
        sum = 0
        # sum is calculated based on where pieces were placed at the end of the round
        for s in range(9):
            if self.spaces[s]:
                sum += self.values[s]
        # The calculated sum is added to the value for each space
        for n in range(9):
            self.values[n] += sum
        # The value of a space where a piece is placed is appended to the string which will be added to history
        for s in range(9):
            if self.spaces[s]:
                tempHistory += str(self.values[s])
        # sum is added at the end to compensate for any strings that might be too short
        while len(tempHistory) < historyLen[len(self.history)]:
            tempHistory += str(sum)
        self.history.append(tempHistory[:historyLen[len(self.history)]])

    def ShowWin(self,winscenario):
        """
        Prints the table with only the winning pieces
        """
        self.PrintBoard()
        input()
        for s in range(9):
            if not str(s) in winscenario:
                self.spaces[s] = False
        self.PrintBoard()

    def EndOfGame(self):
        h = []
        for r in self.history:
            for n in range(len(r)):
                h.append(int(r[n]))
        end = EndGame(h)
        end.DruckenSieDasMasterFlag()