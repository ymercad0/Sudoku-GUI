from sudoku_alg import Sudoku
import pygame
pygame.init()

class Board:
    '''A sudoku board made out of Tiles'''

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

    for i in range (9):
        for j in range (9):
            x = Tile(0,screen,0,1)
            x.draw()

    running = True
    while running:
        for event in pygame.event.get(): #loops through all the pygame events
            if event.type == pygame.QUIT: #if it's a pygame window quit event, pygame stops running
                running = False
main()