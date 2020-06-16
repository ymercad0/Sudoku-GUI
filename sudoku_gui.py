from sudoku_alg import Sudoku
import pygame
pygame.init()

class Tiles:
    '''Represents each white tile/box on the grid'''
    def __init__(self, value, window, x1, x2):
        self.value = value #value of the num on this grid
        self.rows = 9
        self.cols = 9
        self.width = 10
        self.height = 10
        self.window = window #the window/screen we're in
        self.rect = pygame.Rect(x1, x2, self.width, self.height) #dimensions for the rectangles

    def draw(self):
        '''Draws a tile on the board'''
        pygame.draw.rect(self.window, (255,255,255), self.rect)
        pygame.display.update()


#class Board:

def main(): #runs the main Sudoku game
    '''Runs the main Sudoku GUI/Game'''
    screen = pygame.display.set_mode((600, 600))  # make a screen
    pygame.display.set_caption("Sudoku Solver")
    icon = pygame.image.load("icon.png")  # change window image
    pygame.display.set_icon(icon)

    running = True

    for i in range (9):
        for j in range (9):
            x = Tiles(0, screen, i*10, j*10)
            x.draw()


    while running:
        for event in pygame.event.get(): #loops through all the pygame events
            if event.type == pygame.QUIT: #if it's a pygame window quit event, pygame stops running
                running = False


main()