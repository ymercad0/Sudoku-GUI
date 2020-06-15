import numpy as np #to reshape the sudoku grid into a 9x9
class Sudoku:
    '''Initialize a board represented by ints as a 2D Array'''
    def __init__ (self, board):
        '''initialize the board'''
        self.board = board
        self.history = []

    def print_board(self):
        '''Use numpy to reformat board, return None'''
        self.board = np.array(self.board)
        self.board = self.board.reshape(9, 9)
        print(self.board)
        return None

    def find_empty (self):
        '''Finds an empty cell and returns its position as a tuple'''
        for i in range (9):
            for j in range (9):
                if self.board [i][j] == 0:
                    self.pos = (i,j) #0s on the grid
                    self.history.append(self.pos) #keeps track of all the 0 spots
                    return self.pos #return index of the 0 as a tuple

    def on_column (self, num):
        '''Checks if that number is on that same column, returns a bool'''
        for i in range (9):
            if self.board[i][self.pos[1]] == num and (i, self.pos[1]) != self.pos: #make sure it isn't the same number we're checking for by comparing coords
                return True
        return False

    def on_row(self, num):
        '''Checks if a number is on that same row, returns a bool'''
        for j in range (9):
            if self.board[self.pos[0]][j] == num and (self.pos[0],j) != self.pos: #Same row but not same number
                return True
        return False

    def on_grid (self, num):
        ''''Checks if a number is on that grid, returns a bool'''
        start_i = self.pos[0] - self.pos[0]%3 #ex. 5-5%3 = 3 and thats where the grid starts
        start_j = self.pos[1] - self.pos[1]%3

        for i in range (3): # only iterate through a 3x3 grid
            for j in range (3): #adds i and j as needed to go from start of grid to where we need to be
                if self.board[start_i + i][start_j + j] == num and (start_i + i, start_j + j) != self.pos:
                    return True
        return False

    def valid (self, num):
        '''Checks if a number is valid in a grid, column, and row. Returns a Bool'''
        if self.on_column(num) == False and self.on_row(num) == False and self.on_grid(num) == False:
            return True
        return False

    def solve(self): #recursive, once you get to the end of the board it's solved
        '''Solves the Sudoku board, backtrack alg'''
        empty = self.find_empty()
        if not empty: #no empty spots are left so the board is solved
            return True

        for nums in range(9): #try all numbers on a specific spot
            if self.valid(nums+1): #if the number is valid in that grid position
                self.board[self.pos[0]][self.pos[1]] = nums+1
                if self.solve(): #recursive step
                    return True #after assigning a number, if there's no empty spots, returns True

                del self.history[len(self.history) - 1]  #goes back to the last spot, not current
                self.pos = self.history[len(self.history) - 1]  # reassign current position
                self.board[self.pos[0]][self.pos[1]] = 0 #this number is wrong so we set it back to 0
        return False

board = Sudoku([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])

if __name__ == '__main__':
    board.solve()
    board.print_board() #prints the board at the end as a reformated 9x9 array