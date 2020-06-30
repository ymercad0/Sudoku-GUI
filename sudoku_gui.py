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
        '''Fills the board with Tiles and renders their values'''
        for i in range(9):
            for j in range(9):
                if j%3 == 0 and j != 0: #vertical lines
                    pygame.draw.line(self.window, (0, 0, 0), ((j//3)*180, 0), ((j//3)*180, 540), 4)
                    pygame.display.flip()

                if i%3 == 0 and i != 0: #horizontal lines
                    pygame.draw.line(self.window, (0, 0, 0), (0, (i//3)*180), (540, (i//3)*180), 4)
                    pygame.display.flip()

                self.tiles[i][j] = Tile(self.board.get_board()[i][j], self.window, i*60, j*60) #each tile has a distance of 60 units to the other
                self.tiles[i][j].draw((0,0,0), 1)
                if self.board.get_board()[i][j] != 0: #don't draw 0s on the grid
                    self.tiles[i][j].display((20+(j*60), (5+(i*60))))  #20,5 are the coordinates of the first tile
        return self.tiles

class Tile:
    '''Represents each white tile/box on the grid'''
    def __init__(self, value, window, x1, x2):
        self.value = value #value of the num on this grid
        self.window = window
        self.active = False
        self.rect = pygame.Rect(x1, x2, 60, 60) #dimensions for the rectangle

    def draw(self, color, thickness):
        '''Draws a tile on the board'''
        pygame.draw.rect(self.window, color, self.rect, thickness)
        pygame.display.flip()

    def display(self, position):
        '''Displays a number on that tile'''
        font = pygame.font.SysFont('lato', 40)
        text = font.render(str(self.value), True, (0, 0, 0)) #True = antialiasing
        self.window.blit(text, position)
        pygame.display.flip()

    def is_clicked(self, mousePos):
        '''Checks if a tile has been clicked'''
        return self.rect.collidepoint(mousePos) #checks if a user has clicked inside of the Rect coords

def main():
    '''Runs the main Sudoku GUI/Game'''
    screen = pygame.display.set_mode((540, 540))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Sudoku Solver")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    board = Board(screen)
    tiles = board.draw_board() #store the locations of all the tiles on the grid

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                for i in range(9):
                    for j in range (9): #look for tile we clicked on
                        tiles[i][j].draw((0,0,0),1)
                        if tiles[i][j].is_clicked(mousePos):
                            tiles[i][j].draw((50,205,50),4) #redraws that tile but with a highlighted color to show it's been clicked
                            break

main()