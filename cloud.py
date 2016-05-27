import pygame

import constants
from spritesheet import SpriteSheet

class Cloud(pygame.sprite.Sprite):
    last_time = None
    is_next = False
    
    start_image = None
    middle_image = None
    end_image = None

    start = 0
    
    # -- Methods
    def __init__(self, is_next, index):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.is_next = is_next
        self.index = index
        
        self.start_image = pygame.transform.scale(pygame.image.load("cloud-beginning.png"), (constants.BLOCK_SIZE, constants.BLOCK_SIZE * 2))
        self.middle_image = pygame.transform.scale(pygame.image.load("cloud-middle.png"), (constants.BLOCK_SIZE, constants.BLOCK_SIZE * 2))
        self.end_image = pygame.transform.scale(pygame.image.load("cloud-ending.png"), (constants.BLOCK_SIZE, constants.BLOCK_SIZE * 2))
	
    def update(self):
        if self.last_time == None or self.last_time.minute != constants.now.minute:
            self.last_time = constants.now
            self.update_graphics()
        self.rect.x = constants.BLOCK_SIZE * self.start - 2.0 * constants.mario_position / constants.ONE_PIXEL
        if self.is_next: self.rect.x += constants.BLOCK_WIDTH * constants.BLOCK_SIZE

    def update_graphics(self):
        constants.seed = constants.now.minute * constants.now.hour + constants.now.hour * self.index
        if self.is_next: constants.seed += constants.now.hour

        height = constants.random_between(1, 2)
        self.start = constants.random_between(0, constants.BLOCK_WIDTH / 2 - 5);
        if self.index == 1:
            self.start += constants.BLOCK_WIDTH / 2

	length = constants.random_between(1, 3);
		
        self.image = pygame.Surface([constants.BLOCK_SIZE * (length + 2), constants.BLOCK_SIZE * 2], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = constants.BLOCK_SIZE * (height + 1)
        
        self.image.blit(self.start_image, (0, 0), (0, 0, constants.BLOCK_SIZE, constants.BLOCK_SIZE * 2))
        for i in xrange(1, length + 1):
            self.image.blit(self.middle_image, (constants.BLOCK_SIZE * i, 0), (0, 0, constants.BLOCK_SIZE, constants.BLOCK_SIZE * 2))
        self.image.blit(self.end_image, (constants.BLOCK_SIZE * (length + 1), 0), (0, 0, constants.BLOCK_SIZE, constants.BLOCK_SIZE * 2))
