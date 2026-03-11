import pygame
from code.game import Game

if __name__ == '__main__':
    pygame.init()  # O professor sempre coloca isso antes de tudo
    game = Game()
    game.run()