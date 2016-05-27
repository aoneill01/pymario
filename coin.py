import pygame
import constants
from spritesheet import SpriteSheet

class Coin(pygame.sprite.Sprite):
    images = []

    # -- Methods
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("coin.png")
        
        for i in xrange(0, 5):
            self.images.append(sprite_sheet.get_image(i * constants.BLOCK_SIZE, 0, constants.BLOCK_SIZE, constants.BLOCK_SIZE))

        self.image = self.images[0]
	self.rect = self.image.get_rect()
	self.rect.x = constants.BLOCK_SIZE * (constants.BLOCK_WIDTH / 2.0 - .5)
        
    def update(self):
        self.rect.y = constants.BLOCK_SIZE * (constants.BLOCK_HEIGHT - 7.5) + 2 * self.y_position() / constants.ONE_PIXEL
        self.image = self.images[int(constants.time / 3 % 5)]

    def y_position(self):
        # Special handling for skipping this jump.
        if constants.time < constants.FRAMES_PER_SECOND - constants.TIME_TO_APEX or constants.time >= constants.FRAMES_PER_SECOND * 59 + constants.TIME_TO_LAND - constants.TOTAL_WALK_TIME:
            return -constants.HEIGHT;
        
        t = constants.time
        
        t = t % constants.FRAMES_PER_SECOND

        if t < constants.TIME_TO_COIN_BOUNCE and t > 0:
	    return .5 * constants.GRAVITY_NORMAL * t * t + constants.INITIAL_COIN_VELOCITY * t;
	
        return -constants.HEIGHT;
