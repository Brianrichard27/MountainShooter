#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Const import WIN_WIDTH, WINDOW_HEIGHT
from code.background import Background
from code.player import Player
from code.enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level10':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(name=f'Level1{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WINDOW_HEIGHT / 2 - 30))
            case'Player2':
                return Player('Player2', (10, WINDOW_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WINDOW_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WINDOW_HEIGHT - 40)))