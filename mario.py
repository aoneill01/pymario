import pygame
import constants
from spritesheet import SpriteSheet

class Mario(pygame.sprite.Sprite):
    standing = None
    jumping = None
    walking_frames = []

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("mario.png")

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, constants.BLOCK_SIZE, 2 * constants.BLOCK_SIZE)
        self.standing = image

        image = sprite_sheet.get_image(5 * constants.BLOCK_SIZE, 0, constants.BLOCK_SIZE, 2 * constants.BLOCK_SIZE)
        self.jumping = image
        
        for i in xrange(1, 4):
            image = sprite_sheet.get_image(i * constants.BLOCK_SIZE, 0, constants.BLOCK_SIZE, 2 * constants.BLOCK_SIZE)
            self.walking_frames.append(image)
            
        self.walking_frames.append(self.walking_frames[1])
        
        # Set the image the player starts with
        self.image = self.standing

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.y = constants.BLOCK_SIZE * (constants.BLOCK_HEIGHT - 3.5)
        self.rect.x = constants.BLOCK_SIZE * (constants.BLOCK_WIDTH / 2.0 - .5)

    def update(self):
        jump_position = self.jump_position()
        self.rect.y = constants.BLOCK_SIZE * (constants.BLOCK_HEIGHT - 3.5) + 2 * jump_position / constants.ONE_PIXEL
        if jump_position != 0:
            self.image = self.jumping
        elif constants.time < constants.TIME_TO_START_WALKING:
            self.image = self.standing
        else:
            walking_index = int(constants.mario_position / (10 * constants.ONE_PIXEL)) % 4
            self.image = self.walking_frames[walking_index]

    def jump_position(self):
        # Special handling for skipping this jump.
        if constants.time < constants.FRAMES_PER_SECOND - constants.TIME_TO_APEX or constants.time >= constants.FRAMES_PER_SECOND * 59 + constants.TIME_TO_LAND - constants.TOTAL_WALK_TIME:
            return 0;
        
        t = constants.time + constants.TIME_TO_APEX
        
        t = t % constants.FRAMES_PER_SECOND
        
        if t < constants.TIME_TO_APEX:
            return .5 * constants.GRAVITY_HOLDING_A * t * t + constants.INITIAL_JUMP_VELOCITY * t
        
        t -= constants.TIME_TO_APEX;
        if t < constants.TIME_TO_LAND:
            return .5 * constants.GRAVITY_NORMAL * t * t + constants.DISTANCE_TO_APEX
        
        return 0;
