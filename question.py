import pygame
import constants
from spritesheet import SpriteSheet

class Question(pygame.sprite.Sprite):
    last_time = None
    is_next = False
    is_top = False
    
    images = []

    # -- Methods
    def __init__(self, is_next, is_top):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.is_next = is_next
        self.is_top = is_top

        sprite_sheet = SpriteSheet("question-sprite.png")
        
        for i in xrange(0, 6):
            self.images.append(sprite_sheet.get_image(i * constants.BLOCK_SIZE, 0, constants.BLOCK_SIZE, constants.BLOCK_SIZE))

        self.image = self.images[0]
	self.rect = self.image.get_rect()
        
        
    def update(self):
        self.rect.x = constants.BLOCK_SIZE * (constants.BLOCK_WIDTH / 2.0 - .5) - 2.0 * constants.mario_position / constants.ONE_PIXEL
        self.rect.y = constants.BLOCK_SIZE * (constants.BLOCK_HEIGHT - 6.5) + 2 * self.y_position() / constants.ONE_PIXEL
        if self.is_top: self.rect.y -= constants.BLOCK_SIZE * 2
        if self.is_next: self.rect.x += constants.BLOCK_WIDTH * constants.BLOCK_SIZE
        self.image = self.images[int(constants.time / 7 % 5)]

    def y_position(self):
        # Special handling for skipping this jump.
        if self.is_top or constants.time < constants.FRAMES_PER_SECOND - constants.TIME_TO_APEX or constants.time >= constants.FRAMES_PER_SECOND * 59 + constants.TIME_TO_LAND - constants.TOTAL_WALK_TIME:
            return 0;
        
        t = constants.time
        
        t = t % constants.FRAMES_PER_SECOND

        if t < constants.TIME_TO_BLOCK_BOUNCE and t > 0:
	    return .5 * constants.GRAVITY_NORMAL * t * t + constants.INITIAL_BLOCK_VELOCITY * t;
	
        return 0;
