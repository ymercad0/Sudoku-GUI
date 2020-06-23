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

    def draw_board(self):
        '''Fills the board with Tiles'''
        for i in range(9):
            for j in range(9):
                if j%3 == 0 and j != 0: #vertical lines
                    pygame.draw.line(self.window, (0, 0, 0), (((j//3)*180)+1, 0), (((j//3)*180)+1, 540), 5)
                    pygame.display.flip()

                if i%3 == 0 and i != 0: #horizontal lines
                    pygame.draw.line(self.window, (0, 0, 0), (0, ((i//3)*180)+1), (540, ((i//3)*180)+1), 5)
                    pygame.display.flip()

                self.tiles[i][j] = Tile(self.board.get_board()[i][j], self.window, i*60, j*60) #draw a single tile
                self.tiles[i][j].draw()
                self.tiles[i][j].display()

class Tile:
    '''Represents each white tile/box on the grid'''
    def __init__(self, value, window, x1, x2):
        self.value = value #value of the num on this grid
        self.rows = 9
        self.cols = 9
        self.width = 60
        self.height = 60
        self.window = window #the window/screen we're in
        self.rect = pygame.Rect(x1, x2, self.width, self.height) #dimensions for the rectangle

    def draw(self):
        '''Draws a tile on the board'''
        pygame.draw.rect(self.window, (0,0,0), self.rect, 1)
        pygame.display.flip()

    def display(self):
        '''Displays a number on that tile'''
        font = pygame.font.SysFont('arial', 50)
        text = font.render(str(self.value), True, (0, 0, 0))
        rect = text.get_rect() #Returns a new rectangle covering the entire surface
        self.window.blit(text, rect)
        pygame.display.update()

def main():
    '''Runs the main Sudoku GUI/Game'''
    screen = pygame.display.set_mode((540, 540))  # make a screen
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Sudoku Solver")
    icon = pygame.image.load("icon.png")  # change window image
    pygame.display.set_icon(icon)

    y = Board(screen)
    y.draw_board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()