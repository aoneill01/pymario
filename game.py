import pygame
from datetime import datetime
import os
import sys
import time
import constants
from mario import Mario
from ground import Ground
from bricktime import BrickTime
from bush import Bush
from cloud import Cloud
from question import Question
from datesec import DateSec
from coin import Coin

pygame.init()

clock = pygame.time.Clock()
constants.update()

screen = pygame.display.set_mode((constants.BLOCK_WIDTH * constants.BLOCK_SIZE, constants.BLOCK_HEIGHT * constants.BLOCK_SIZE), pygame.FULLSCREEN)

active_sprite_list_1 = pygame.sprite.Group()
active_sprite_list_1.add(Question(True, False))
active_sprite_list_1.add(Question(False, False))
active_sprite_list_1.add(Question(True, True))
active_sprite_list_1.add(Question(False, True))
active_sprite_list_1.add(Bush(False))
active_sprite_list_1.add(Bush(True))
active_sprite_list_1.add(Cloud(False, 0))
active_sprite_list_1.add(Cloud(True, 0))
active_sprite_list_1.add(Cloud(False, 1))
active_sprite_list_1.add(Cloud(True, 1))
active_sprite_list_1.add(Ground())
active_sprite_list_1.add(DateSec())
active_sprite_list_2 = pygame.sprite.Group()
active_sprite_list_2.add(Mario())
active_sprite_list_2.add(BrickTime(False))
active_sprite_list_2.add(BrickTime(True))
active_sprite_list_2.add(Coin())
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: sys.exit()

    active_sprite_list_1.update()
    active_sprite_list_2.update()
    screen.fill(constants.SKY_COLOR)
    active_sprite_list_1.draw(screen)
    active_sprite_list_2.draw(screen)

    constants.update()
    #text = font.render(str(constants.mario_position) + " " + str(constants.time), 1, (10, 10, 10))
    #textpos = text.get_rect()
    #screen.blit(text, textpos)
    
    pygame.display.flip()
    
    clock.tick(60)

