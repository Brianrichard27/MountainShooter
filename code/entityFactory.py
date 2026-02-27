#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame.examples.grid import WINDOW_WIDTH

from code.Const import WIN_WIDTH
from code.background import Background # Importa a classe do arquivo correto

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