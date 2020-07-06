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
        self.tiles = [[Tile(self.board.get_board()[i][j], window, i*60, j*60) for i in range(9)] for j in range(9)]
        self.window = window

    def draw_board(self):
        '''Fills the board with Tiles and renders their values'''
        for i in range(9):
            for j in range(9):
                if j%3 == 0 and j != 0: #vertical lines
                    pygame.draw.line(self.window, (0, 0, 0), ((j//3)*180, 0), ((j//3)*180, 540), 4)

                if i%3 == 0 and i != 0: #horizontal lines
                    pygame.draw.line(self.window, (0, 0, 0), (0, (i//3)*180), (540, (i//3)*180), 4)

                self.tiles[i][j].draw((0,0,0), 1)

                if self.board.get_board()[i][j] != 0: #don't draw 0s on the grid
                    self.tiles[i][j].display((20+(j*60), (5+(i*60))))  #20,5 are the coordinates of the first tile
        return self.tiles

    def deselect(self, tile):
        '''Deselects every tile except the one currently clicked'''
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j] != tile:
                    self.tiles[i][j].undo_select()

    def redraw(self):
        '''Redraws board with highlighted tiles'''
        self.window.fill((255,255,255))
        self.draw_board()
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j].is_selected():  # draws the green border on selected tiles
                    self.tiles[i][j].draw((50, 205, 50), 5)

class Tile:
    '''Represents each white tile/box on the grid'''
    def __init__(self, value, window, x1, y1):
        self.value = value #value of the num on this grid
        self.window = window
        self.rect = pygame.Rect(x1, y1, 60, 60) #dimensions for the rectangle
        self.selected = False

    def draw(self, color, thickness):
        '''Draws a tile on the board'''
        pygame.draw.rect(self.window, color, self.rect, thickness)

    def display(self, position):
        '''Displays a number on that tile'''
        font = pygame.font.SysFont('lato', 40)
        text = font.render(str(self.value), True, (0, 0, 0)) #True = antialiasing
        self.window.blit(text, position)

    def clicked(self, mousePos):
        '''Checks if a tile has been clicked'''
        if self.rect.collidepoint(mousePos): #checks if a point is inside a rect
            self.selected = True
        return self.selected

    def undo_select(self):
        ''''Resets an unselected tile'''
        self.selected = False

    def is_selected(self):
        return self.selected

def main():
    '''Runs the main Sudoku GUI/Game'''
    screen = pygame.display.set_mode((540, 540))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Sudoku Solver")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    board = Board(screen)
    tiles = board.draw_board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                for i in range(9):
                    for j in range (9):
                        if tiles[i][j].clicked(mousePos):
                            board.deselect(tiles[i][j]) #deselects every tile except the one currently clicked

        board.redraw()
        pygame.display.flip()
main()
pygame.quit()