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
        self.tiles = [[Tile(self.board.get_board()[i][j], window, i*60, j*60) for j in range(9)] for i in range(9)]
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

                if self.tiles[i][j].value != 0: #don't draw 0s on the grid
                    self.tiles[i][j].display(self.tiles[i][j].value, (20+(j*60), (5+(i*60))), (0, 0, 0))  #20,5 are the coordinates of the first tile

    def deselect(self, tile):
        '''Deselects every tile except the one currently clicked'''
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j] != tile:
                    self.tiles[i][j].selected = False

    def redraw(self, keys):
        '''Redraws board with highlighted tiles'''
        self.window.fill((255,255,255))
        self.draw_board()
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j].selected:  # draws the green border on selected tiles and displays greyed out num
                    self.tiles[i][j].draw((50, 205, 50), 4)

        if len(keys) != 0: #draws inputs that the user places on board but not their final value picls on that tile
            for value in keys:
                self.tiles[value[0]][value[1]].display(keys[value], (20+(value[0]*60), (5+(value[1]*60))), (128, 128, 128))
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

    def display(self, value, position, color):
        '''Displays a number on that tile'''
        font = pygame.font.SysFont('lato', 40)
        text = font.render(str(value), True, color) #True = antialiasing
        self.window.blit(text, position)

    def clicked(self, mousePos):
        '''Checks if a tile has been clicked'''
        if self.rect.collidepoint(mousePos): #checks if a point is inside a rect
            self.selected = True
        return self.selected

def main():
    '''Runs the main Sudoku GUI/Game'''
    screen = pygame.display.set_mode((540, 540))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Sudoku Solver")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    board = Board(screen)
    keyDict = {}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                for i in range(9):
                    for j in range (9):
                        if board.tiles[i][j].clicked(mousePos):
                            selected = i,j
                            board.deselect(board.tiles[i][j]) #deselects every tile except the one currently clicked

            elif event.type == pygame.KEYDOWN: #when a keyboard key is pressed
                if board.board.get_board()[selected[1]][selected[0]] == 0:
                    if event.key == pygame.K_1:
                        key = 1
                        keyDict[selected] = 1

                    if event.key == pygame.K_2:
                        key = 2
                        keyDict[selected] = 2

                    if event.key == pygame.K_3:
                        key = 3
                        keyDict[selected] = 3

                    if event.key == pygame.K_4:
                        key = 4
                        keyDict[selected] = 4

                    if event.key == pygame.K_5:
                        key = 5
                        keyDict[selected] = 5

                    if event.key == pygame.K_6:
                        key = 6
                        keyDict[selected] = 6

                    if event.key == pygame.K_7:
                        key = 7
                        keyDict[selected] = 7

                    if event.key == pygame.K_8:
                        key = 8
                        keyDict[selected] = 8

                    if event.key == pygame.K_9:
                        key = 9
                        keyDict[selected] = 9

                    elif event.key == pygame.K_RETURN:
                        if len(keyDict) != 0:
                            board.tiles[selected[1]][selected[0]].value = keyDict[selected] #assigns current grid value not to current key but to curent greyed out highlighted value
                            del keyDict[selected]
                            break
                        try: #in case user presses down on an empty tile at the start
                            board.tiles[selected[1]][selected[0]].value = key
                        except UnboundLocalError:
                            continue

        board.redraw(keyDict)
        pygame.display.flip()
main()
pygame.quit()