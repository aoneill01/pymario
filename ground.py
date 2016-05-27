import pygame
import math
import constants
from spritesheet import SpriteSheet

class Ground(pygame.sprite.Sprite):

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        stone = pygame.image.load("stone.png")
        stone = pygame.transform.scale(stone, (32, 32))

        self.image = pygame.Surface([constants.BLOCK_SIZE * (constants.BLOCK_WIDTH + 1), constants.BLOCK_SIZE * 1.5], pygame.SRCALPHA, 32).convert_alpha()
        for i in xrange(0, int(math.ceil(constants.BLOCK_WIDTH + 1))):
            for j in xrange(0, 3):
                self.image.blit(stone, (i * constants.BLOCK_SIZE, j * constants.BLOCK_SIZE), (0, 0, constants.BLOCK_SIZE, constants.BLOCK_SIZE))
        
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.y = constants.BLOCK_SIZE * constants.BLOCK_HEIGHT - self.rect.height

    def update(self):
        #millis = int(round(time.time() * 1000))
        
        self.rect.x = -2.0 * constants.mario_position / constants.ONE_PIXEL
        while self.rect.x < -32:
            self.rect.x += 32
