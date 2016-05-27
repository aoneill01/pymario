import pygame
import time
import datetime
import constants
from spritesheet import SpriteSheet

NUMBERS = [
    [
            [ True, True, True ],
            [ True, False, True ],
            [ True, False, True ],
            [ True, False, True ],
            [ True, True, True ]
    ],
    [
            [ False, False, True ],
            [ False, False, True ],
            [ False, False, True ],
            [ False, False, True ],
            [ False, False, True ]
    ],
    [
            [ True, True, True ],
            [ False, False, True ],
            [ True, True, True ],
            [ True, False, False ],
            [ True, True, True ]
    ],
    [
            [ True, True, True ],
            [ False, False, True ],
            [ False, True, True ],
            [ False, False, True ],
            [ True, True, True ]
    ],
    [
            [ True, False, True ],
            [ True, False, True ],
            [ True, True, True ],
            [ False, False, True ],
            [ False, False, True ]
    ],
    [
            [ True, True, True ],
            [ True, False, False ],
            [ True, True, True ],
            [ False, False, True ],
            [ True, True, True ]
    ],
    [
            [ True, True, True ],
            [ True, False, False ],
            [ True, True, True ],
            [ True, False, True ],
            [ True, True, True ]
    ],
    [
            [ True, True, True ],
            [ False, False, True ],
            [ False, False, True ],
            [ False, False, True ],
            [ False, False, True ]
    ],
    [
            [ True, True, True ],
            [ True, False, True ],
            [ True, True, True ],
            [ True, False, True ],
            [ True, True, True ]
    ],
    [
            [ True, True, True ],
            [ True, False, True ],
            [ True, True, True ],
            [ False, False, True ],
            [ True, True, True ]
    ]
]

class BrickTime(pygame.sprite.Sprite):
    last_time = None
    is_next = False
    
    brick1 = None
    brick2 = None
    
    # -- Methods
    def __init__(self, is_next):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.last_time = constants.now
        self.is_next = is_next
        
        self.brick1 = pygame.transform.scale(pygame.image.load("brick.png"), (constants.BLOCK_SIZE, constants.BLOCK_SIZE))
	self.brick2 = pygame.transform.scale(pygame.image.load("brick-interior.png"), (constants.BLOCK_SIZE, constants.BLOCK_SIZE))

	self.updateBricks()

    def update(self):
        if self.last_time.minute != constants.now.minute:
            self.last_time = constants.now
            self.updateBricks()
        self.rect.x = constants.BLOCK_SIZE * (constants.BLOCK_WIDTH / 2.0 - 8.5) - 2.0 * constants.mario_position / constants.ONE_PIXEL
        if self.is_next: self.rect.x += constants.BLOCK_WIDTH * constants.BLOCK_SIZE
    
    def updateBricks(self):
        self.image = pygame.Surface([constants.BLOCK_SIZE * (3 * 4 + 5), constants.BLOCK_SIZE * 5], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = constants.BLOCK_SIZE * 4.5
        time = self.last_time + datetime.timedelta(seconds=60) if self.is_next else self.last_time
        hour = time.hour % 12
        if hour == 0: hour = 12
        if hour / 10 > 0:
            self.drawDigit(hour / 10, 0)
        self.drawDigit(hour % 10, 4)
        self.drawDigit(time.minute / 10, 10)
        self.drawDigit(time.minute % 10, 14)
        
    def drawDigit(self, digit, offset):
        for y in xrange(5):
            for x in xrange(3):
                if NUMBERS[digit][y][x]:
                    self.image.blit(self.brick2 if y > 0 and NUMBERS[digit][y - 1][x] else self.brick1, ((x + offset) * constants.BLOCK_SIZE, y * constants.BLOCK_SIZE), (0, 0, constants.BLOCK_SIZE, constants.BLOCK_SIZE))
