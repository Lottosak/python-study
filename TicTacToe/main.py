import imp
import pygame
from pygame.locals import *
import math

class Board:
    def __init__(self, size):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.size = size
        self.square = (math.floor(size[0]/3), math.floor(size[1]/3))

    def drawBackground(self, surface):
        surface.fill((255, 255, 255))

        pygame.draw.line(surface, (0, 0, 0), (self.square[0], 0), (self.square[0], self.size[1]))
        pygame.draw.line(surface, (0, 0, 0), (self.square[0]*2, 0), (self.square[0]*2, self.size[1]))
        pygame.draw.line(surface, (0, 0, 0), (0, self.square[1]), (self.size[0], self.square[1]))
        pygame.draw.line(surface, (0, 0, 0), (0, self.square[1]*2), (self.size[0], self.square[1]*2))

    def getIndexFromPosition(self, position):
        col = math.floor(position[0] / self.square[0])
        row = math.floor(position[1] / self.square[1])  
        return (col, row)

    def drawCross(self, surface, position):
        idx = self.getIndexFromPosition(position)

        startPos = (self.square[0] * idx[0], self.square[1] * idx[1])
        endPos = (self.square[0] * idx[0] + self.square[0], self.square[1] * idx[1] + self.square[1])

        pygame.draw.line(surface,(255, 0, 0), startPos, endPos, 3)

        startPos = (self.square[0] * idx[0], self.square[1] * idx[1] + self.square[1])
        endPos = (self.square[0] * idx[0] + self.square[0], self.square[1] * idx[1])

        pygame.draw.line(surface,(255, 0, 0), startPos, endPos, 3)

    def drawCircle(self, surface, position):
        idx = self.getIndexFromPosition(position)

        pos = (self.square[0] * idx[0] + math.floor(self.square[0]/2), self.square[1] * idx[1] + math.floor(self.square[1]/2))

        radius = math.floor(min(self.square)/2)

        pygame.draw.circle(surface, (0, 0, 255), pos, radius, 3)

    def updateBoardState(self, position, cross):
        idx = self.getIndexFromPosition(position)

        print(self.board)

        if self.board[idx[1]][idx[0]] != 0:
            return False

        if cross:
            self.board[idx[1]][idx[0]] = 1
        else:
            self.board[idx[1]][idx[0]] = 2
        
        return True


    def checkVictory(self):
        #simple check, to lazy to think something more inteligent
        #check cols 
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != 0:
            return True
        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][1] != 0:
            return True
        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] != 0:
            return True

        #check rows
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] != 0:
            return True
        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][0] != 0:
            return True
        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] != 0:
            return True

        #check diagonals
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            return True

        return False

    def checkDraw(self):
        for row in self.board:
            for val in row:
                if val == 0:
                    return False
        return True

class GameManager:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.fps = None
        self.board = Board(self.size)
        self.playerOne = True
        self.enable = True
        self.font = None

    def on_init(self):
        pygame.init()
        pygame. font.init()

        self.font = pygame.font.Font(None, 100)
        pygame.display.set_caption("TicTacToe")

        self.fps = pygame.time.Clock()
        self.display_surf = pygame.display.set_mode(self.size)
        self.running = True

        self.board.drawBackground(self.display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.MOUSEBUTTONUP and self.enable:
            pos = pygame.mouse.get_pos()

            update = self.board.updateBoardState(pos, self.playerOne)

            if update:
                if self.playerOne:
                    self.board.drawCross(self.display_surf, pos)
                else:
                    self.board.drawCircle(self.display_surf, pos)

                if self.board.checkVictory():
                    self.enable = False
                    self.display_surf.blit(self.font.render("Victory", False, (0, 255, 0)), (0, 0))
                
                if self.board.checkDraw():
                    self.enable = False
                    self.display_surf.blit(self.font.render("Draw", False, (0, 255, 0)), (0, 0))

                self.playerOne = not self.playerOne

            print(pos)
    
    def on_loop(self):
        pygame.display.update()
        self.fps.tick(30)

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
        
        self.on_cleanup()


if __name__ == "__main__":

    game = GameManager()
    game.on_execute()