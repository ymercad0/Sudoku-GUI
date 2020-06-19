from sudoku_alg import Sudoku
import pygame
pygame.init()

class Board:
    '''A sudoku board made out of Tiles'''
    def __init__(self, window):
        self.window = window
        self.tiles = []

    def fill_board(self):
        '''Fills the board with Tiles'''
        for i in range(9):
            for j in range(9):
                self.tiles.append(Tile(0, self.window, i*61, j*61))
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
        pygame.draw.rect(self.window, (255,255,255), self.rect)
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
        for event in pygame.event.get(): #loops through all the pygame events
            if event.type == pygame.QUIT: #if it's a pygame window quit event, pygame stops running
                running = False
main()