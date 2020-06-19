from sudoku_alg import Sudoku
import pygame
pygame.init()

class Board:
    '''A sudoku board made out of Tiles'''
    def __init__(self, window):
        self.board = Sudoku([
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
        self.window = window
        self.tiles = [[0 for i in range(9)] for j in range(9)]

    def fill_board(self):
        '''Fills the board with Tiles'''
        for i in range(9):
            for j in range(9):
                self.tiles[i][j] = Tile(self.board.get_board()[i][j], self.window, i*60, j*60)
                self.tiles[i][j].draw()

class Tile:
    '''Represents each white tile/box on the grid'''
    def __init__(self, value, window, x1, x2):
        self.value = value #value of the num on this grid
        self.rows = 9
        self.cols = 9
        self.width = 60
        self.height = 60
        self.window = window #the window/screen we're in
        self.rect = pygame.Rect(x1, x2, self.width, self.height) #dimensions for the rectangles

    def draw(self):
        '''Draws a tile on the board'''
        pygame.draw.rect(self.window, (255,255,255), self.rect, 1)
        pygame.display.update()
        
def main():
    '''Runs the main Sudoku GUI/Game'''
    screen = pygame.display.set_mode((540, 540))  # make a screen
    pygame.display.set_caption("Sudoku Solver")
    icon = pygame.image.load("icon.png")  # change window image
    pygame.display.set_icon(icon)

    y = Board(screen)
    y.fill_board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()