import datetime
import math

BLOCK_WIDTH = 23
BLOCK_HEIGHT = 14
BLOCK_SIZE = 32

SKY_COLOR = (107, 140, 255)

# Units are in the hex form blocks-pixels-subpixels-subsubpixels-subsubsubpixels where each level is 1/16 the previous.
# Positions are relative to the top left corner.
ONE_BLOCK = 0x10000
ONE_PIXEL = 0x01000
#SPRITE_SIZE = ONE_BLOCK
# Width of visible screen.
WIDTH = BLOCK_WIDTH * ONE_BLOCK
# Height of screen, though the bottom block isn't completely displayed.
HEIGHT = BLOCK_HEIGHT * ONE_BLOCK

# Physics is based on updates 60 times per second, though rendered frames may be more or less than this.
FRAMES_PER_SECOND = 60
#MILLISECONDS_PER_SECOND = 1000
INITIAL_WALK_VELOCITY = 0x00130
MAX_WALK_VELOCITY = 0x01800 # or 0x02900 for running
WALK_ACCELERATION = 0x00098 # or 0x000E4 for running
WALK_DECELERATION = -0x000D0

# Pre-calculate some constant values for the movements.
# Based on the following equations:
# v = a*t + v0
# x = .5*a*t*t + v0*t + x0

# Walking physics.
# Time to reach maximum velocity.
TIME_TO_MAX_WALK_VELOCITY = (MAX_WALK_VELOCITY - INITIAL_WALK_VELOCITY) / WALK_ACCELERATION
# Distance travelled by the time maximum velocity was reached.
DISTANCE_TO_MAX_WALK_VELOCITY = int(.5 * WALK_ACCELERATION * TIME_TO_MAX_WALK_VELOCITY * TIME_TO_MAX_WALK_VELOCITY + INITIAL_WALK_VELOCITY * TIME_TO_MAX_WALK_VELOCITY)
# Time to come to a stop from maximum velocity.
TIME_TO_DECELERATE = -MAX_WALK_VELOCITY / WALK_DECELERATION
# Distance travelled to stop.
DISTANCE_TO_DECELERATE = int(.5 * WALK_DECELERATION * TIME_TO_DECELERATE * TIME_TO_DECELERATE + MAX_WALK_VELOCITY * TIME_TO_DECELERATE)
# Assuming Mario reaches maximum velocity, the distance Mario needs to cover at maximum velocity before needing to decelerate.
DISTANCE_TO_WALK = WIDTH - DISTANCE_TO_MAX_WALK_VELOCITY - DISTANCE_TO_DECELERATE
# Time walking at maximum velocity.
TIME_TO_WALK = DISTANCE_TO_WALK / MAX_WALK_VELOCITY
# Total walking time from one screen to the next.
TOTAL_WALK_TIME = TIME_TO_MAX_WALK_VELOCITY + TIME_TO_DECELERATE + TIME_TO_WALK
# When to start walking so that Mario will be done at the beginning of the minute.
TIME_TO_START_WALKING = 60 * FRAMES_PER_SECOND - TOTAL_WALK_TIME

# X-position that Mario starts at.
#START_POSITION = WIDTH / 2
# Mario's y-position when standing on the ground.
GROUND_POSITION = 11 * ONE_BLOCK

# Jumping physics.
INITIAL_JUMP_VELOCITY = -0x04000
# Gravity is lower when holding A while jumping.
GRAVITY_HOLDING_A = 0x00200
# Normal falling gravity.
GRAVITY_NORMAL = 0x00700
# Time to reach the top of Mario's jump. This is a hard stop when he hits the ? block.
TIME_TO_APEX = (-INITIAL_JUMP_VELOCITY - math.sqrt(INITIAL_JUMP_VELOCITY * INITIAL_JUMP_VELOCITY - 4 * .5 * GRAVITY_HOLDING_A * 0x20000)) / (2 * .5 * GRAVITY_HOLDING_A) 
# Distance to the top of Mario's jump.
DISTANCE_TO_APEX = int(.5 * GRAVITY_HOLDING_A * TIME_TO_APEX * TIME_TO_APEX + INITIAL_JUMP_VELOCITY * TIME_TO_APEX)
# Time for gravity to bring Mario back to the ground.
TIME_TO_LAND = math.sqrt(-2*DISTANCE_TO_APEX/GRAVITY_NORMAL)
 
# Physics for ? block.
INITIAL_BLOCK_VELOCITY = -0x02800
TIME_TO_BLOCK_BOUNCE = -2*INITIAL_BLOCK_VELOCITY / GRAVITY_NORMAL

# Physics for coin popping into the air.
INITIAL_COIN_VELOCITY = -0x05C00
TIME_TO_COIN_BOUNCE = -2*INITIAL_COIN_VELOCITY / GRAVITY_NORMAL

time = 0
mario_position = 0
now = None

def update():
    globals()["now"] = datetime.datetime.now()
    globals()["time"] = FRAMES_PER_SECOND * (now.second + now.microsecond / 1000000.0)
    globals()["mario_position"] = calculate_mario_position()

def calculate_mario_position():
    t = time
    if (t < TIME_TO_START_WALKING):
        return 0
    t -= TIME_TO_START_WALKING
    if (t < TIME_TO_MAX_WALK_VELOCITY):
        return .5 * WALK_ACCELERATION * t * t + INITIAL_WALK_VELOCITY * t
    t -= TIME_TO_MAX_WALK_VELOCITY
    if (t < TIME_TO_WALK):
        return MAX_WALK_VELOCITY * t + DISTANCE_TO_MAX_WALK_VELOCITY
    t -= TIME_TO_WALK
    return .5 * WALK_DECELERATION * t * t + MAX_WALK_VELOCITY * t + DISTANCE_TO_MAX_WALK_VELOCITY + DISTANCE_TO_WALK

seed = 1

def random():
    seed = globals()["seed"]
    seed += 1
    globals()["seed"] = seed
    x = math.sin(seed) * 10000
    return x - math.floor(x)

def random_between(a, b):
    r = random()
    return int((1 + b - a) * random() + a)
