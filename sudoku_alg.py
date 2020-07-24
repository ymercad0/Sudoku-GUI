import random
from copy import deepcopy
def generate():
    '''Randomly generates a Sudoku grid/board'''
    while True:  #return will interrupt the loop
        board = Sudoku([ #recursion is really slow and inneficient
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        # puts one random number, then solves the board to generate a board
        for i in range(9):
            for j in range(9):
                if random.randint(1, 10) >= 5:
                    board.board[i][j] = random.randint(1, 9)  #plug in random number at random spot
                    if board.valid((i, j), board.board[i][j]):
                        continue
                    else:
                        board.board[i][j] = 0

        partialBoard = deepcopy(board) #copies board without being modified after .solve is called
        if board.solve():
            return partialBoard

class Sudoku:
    '''Initialize a board represented by ints as a 2D Array'''
    def __init__ (self, board):
        '''Initialize the board'''
        self.board = board

    def print_board(self):
        '''Prints the board'''
        boardString = ""
        for i in range(9):
            for j in range(9):
                boardString += str(self.board[i][j]) + " "
                if (j+1)%3 == 0 and j != 0 and (j+1) != 9:
                    boardString += "| "

                if j == 8:
                    boardString += "\n"

                if j == 8 and (i+1)%3 == 0 and (i+1) != 9:
                    boardString += "- - - - - - - - - - - \n"
        print(boardString)

    def find_empty (self):
        '''Finds an empty cell and returns its position as a tuple'''
        for i in range (9):
            for j in range (9):
                if self.board[i][j] == 0:
                    return i,j

    def valid(self, pos, num):
        '''Whether a number is valid in that cell, returns a bool'''
        for i in range(9):
            if self.board[i][pos[1]] == num and (i, pos[1]) != pos:  #make sure it isn't the same number we're checking for by comparing coords
                return False

        for j in range(9):
            if self.board[pos[0]][j] == num and (pos[0], j) != pos:  #Same row but not same number
                return False

        start_i = pos[0] - pos[0] % 3 #ex. 5-5%3 = 3 and thats where the grid starts
        start_j = pos[1] - pos[1] % 3
        for i in range(3):
            for j in range(3):  #adds i and j as needed to go from start of grid to where we need to be
                if self.board[start_i + i][start_j + j] == num and (start_i + i, start_j + j) != pos:
                    return False
        return True

    def get_board(self):
        '''Returns the board not as an instance of Sudoku but as a 2D array'''
        return self.board

    def solve(self):
        '''Solves the Sudoku board via the backtracking algorithm'''
        empty = self.find_empty()
        if not empty: #no empty spots are left so the board is solved
            return True

        for nums in range(9):
            if self.valid(empty,nums+1):
                self.board[empty[0]][empty[1]] = nums+1

                if self.solve(): #recursive step
                    return True
                self.board[empty[0]][empty[1]] = 0 #this number is wrong so we set it back to 0
        return False

if __name__ == '__main__':
    board = generate()
    board.solve()
    board.print_board()