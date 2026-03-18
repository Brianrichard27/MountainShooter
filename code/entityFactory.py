#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Const import WIN_WIDTH, WINDOW_HEIGHT
from code.PlayerShot import PlayerShot
from code.background import Background
from code.player import Player
from code.enemy import Enemy
from code.PlayerShot import PlayerShot

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
         match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(name=f'Level2Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level2Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WINDOW_HEIGHT / 2 - 30))
            case'Player2':
                return Player('Player2', (10, WINDOW_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WINDOW_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WINDOW_HEIGHT - 40)))
            case 'Player1Shot':
                return PlayerShot(name='Player1Shot', position=position)
            case 'Player2Shot':
                return PlayerShot(name='Player2Shot', position=position)
         return None