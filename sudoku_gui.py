from sudoku_alg import Sudoku
from sys import exit
import pygame
import time
pygame.init()

class Board:
    '''A sudoku board made out of Tiles'''
    def __init__(self, window):
        self.board = Sudoku([
        [0, 3, 0, 0, 1, 0, 0, 6, 0],
        [0, 2, 0, 0, 0, 4, 0, 0, 0],
        [1, 0, 0, 0, 0, 3, 5, 0, 0],
        [3, 0, 0, 0, 9, 0, 0, 0, 0],
        [8, 6, 0, 0, 0, 0, 0, 4, 1],
        [0, 0, 0, 0, 7, 0, 0, 0, 8],
        [0, 0, 5, 9, 0, 0, 0, 0, 2],
        [0, 0, 0, 1, 0, 0, 0, 9, 0],
        [0, 4, 0, 0, 8, 0, 0, 5, 0]
    ])
        self.solvedBoard = Sudoku([row[:] for row in self.board.get_board()])
        self.solvedBoard.solve() #so that self.board isn't modified
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
                if self.tiles[j][i].selected:  #draws the green border on selected tiles
                    self.tiles[j][i].draw((50, 205, 50), 4)

                elif self.tiles[i][j].correct:
                    self.tiles[j][i].draw((34, 139, 34), 4)

                elif self.tiles[i][j].incorrect:
                    self.tiles[j][i].draw((255, 0, 0), 4)

        if len(keys) != 0: #draws inputs that the user places on board but not their final value on that tile
            for value in keys:
                self.tiles[value[0]][value[1]].display(keys[value], (20+(value[0]*60), (5+(value[1]*60))), (128, 128, 128))
        pygame.display.flip()

    def visualSolve(self):
        '''Showcases how the board is solved via backtracking'''
        empty = self.board.find_empty()
        if not empty:
            return True

        for nums in range(9):
            if self.board.valid((empty[0],empty[1]), nums+1):
                self.board.get_board()[empty[0]][empty[1]] = nums+1
                self.tiles[empty[0]][empty[1]].value = nums+1
                self.tiles[empty[0]][empty[1]].correct = True
                pygame.time.delay(63) #show tiles at a slower rate
                self.redraw({})

                if self.visualSolve():
                    return True

                self.board.get_board()[empty[0]][empty[1]] = 0
                self.tiles[empty[0]][empty[1]].value = 0
                self.tiles[empty[0]][empty[1]].incorrect = True
                self.tiles[empty[0]][empty[1]].correct = False
                pygame.time.delay(63)
                self.redraw({})

class Tile:
    '''Represents each white tile/box on the grid'''
    def __init__(self, value, window, x1, y1):
        self.value = value #value of the num on this grid
        self.window = window
        self.rect = pygame.Rect(x1, y1, 60, 60) #dimensions for the rectangle
        self.selected = False
        self.correct = False
        self.incorrect = False

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
    selected = -1,-1 #NoneType error when selected = None, easier to just format as a tuple whose value will never be used
    keyDict = {}

    running = True
    while running:
        if board.board.get_board() == board.solvedBoard.get_board(): #user has solved the board
            for i in range(9):
                for j in range(9):
                    board.tiles[i][j].selected = False
                    running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() #so that it doesnt go to the outer run loop

            elif event.type == pygame.MOUSEBUTTONUP: #allow clicks only while the board hasn't been solved
                mousePos = pygame.mouse.get_pos()
                for i in range(9):
                    for j in range (9):
                        if board.tiles[i][j].clicked(mousePos):
                            selected = i,j
                            board.deselect(board.tiles[i][j]) #deselects every tile except the one currently clicked

            elif event.type == pygame.KEYDOWN:
                if board.board.get_board()[selected[1]][selected[0]] == 0 and selected != (-1,-1):
                    if event.key == pygame.K_1:
                        keyDict[selected] = 1

                    if event.key == pygame.K_2:
                        keyDict[selected] = 2

                    if event.key == pygame.K_3:
                        keyDict[selected] = 3

                    if event.key == pygame.K_4:
                        keyDict[selected] = 4

                    if event.key == pygame.K_5:
                        keyDict[selected] = 5

                    if event.key == pygame.K_6:
                        keyDict[selected] = 6

                    if event.key == pygame.K_7:
                        keyDict[selected] = 7

                    if event.key == pygame.K_8:
                        keyDict[selected] = 8

                    if event.key == pygame.K_9:
                        keyDict[selected] = 9

                    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:  # clears tile out
                        if selected in keyDict:
                            board.tiles[selected[1]][selected[0]].value = 0
                            del keyDict[selected]

                    elif event.key == pygame.K_RETURN:
                        if selected in keyDict:
                            if keyDict[selected] != board.solvedBoard.get_board()[selected[1]][selected[0]]: #clear tile when incorrect value is inputted
                                board.tiles[selected[1]][selected[0]].value = 0
                                del keyDict[selected]
                                break
                            #valid and correct entry into cell
                            board.tiles[selected[1]][selected[0]].value = keyDict[selected] #assigns current grid value
                            board.board.get_board()[selected[1]][selected[0]] = keyDict[selected] #assigns to actual board so that the correct value can't be modified
                            del keyDict[selected]

                if event.key == pygame.K_SPACE:
                    for i in range(9):
                        for j in range(9):
                            board.tiles[i][j].selected = False
                    keyDict = {}  # clear keyDict out
                    board.redraw(keyDict)
                    board.visualSolve()
                    for i in range(9):
                        for j in range(9):
                            board.tiles[i][j].correct = False
                            board.tiles[i][j].incorrect = False #reset tiles
                    running = False

        board.redraw(keyDict)

    while True: #another running loop so that the program ONLY closes when user closes program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
main()
pygame.quit()