import pygame
import constants
from spritesheet import SpriteSheet

class DateSec(pygame.sprite.Sprite):
    digits = []
    
    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.title = pygame.image.load("date-sec-title.png")
        self.title = pygame.transform.scale(self.title, (160, 14))

        sprite_sheet = SpriteSheet("numbers.png")
        for i in xrange(0, 11):
            self.digits.append(sprite_sheet.get_image(i * 16, 0, 16, 14))

        self.image = pygame.Surface([160, 32], pygame.SRCALPHA, 32).convert_alpha()
        self.image.blit(self.title, (0, 0), (0, 0, 160, 14))
        #self.image.blit(self.digits[3], (0, 16), (0, 0, 16, 14))
        
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.y = 8
        self.rect.x = constants.BLOCK_WIDTH * constants.BLOCK_SIZE - 176

    def update(self):
        seconds = constants.now.second
        month = constants.now.month
        day = constants.now.day
        
        self.image.blit(self.digits[month/10], (0, 16), (0, 0, 16, 14))
        self.image.blit(self.digits[month%10], (16, 16), (0, 0, 16, 14))
        self.image.blit(self.digits[10], (32, 16), (0, 0, 16, 14))
        self.image.blit(self.digits[day/10], (48, 16), (0, 0, 16, 14))
        self.image.blit(self.digits[day%10], (64, 16), (0, 0, 16, 14))
        
        self.image.blit(self.digits[seconds/10], (128, 16), (0, 0, 16, 14))
        self.image.blit(self.digits[seconds%10], (144, 16), (0, 0, 16, 14))
        
