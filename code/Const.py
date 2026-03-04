#C
import pygame

COLOR_ORANGE = (255,128,0)
COLOR_YELLOW = (255, 215, 0)
COLOR_WHITE = (255, 255, 255)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED =  {
    'Level10' : -0,
    'Level11' : 1,
    'Level12' : 2,
    'Level13' : 3,
    'Player1' : 3,
    'Player2' : 3,
    'Enemy1' : 2,
    'Enemy2' : 1,


}


#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 3P - COMPETITIVE',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}



#S
SPAWN_TIME = 4000




# W

WIN_WIDTH = 576
WINDOW_HEIGHT = 324