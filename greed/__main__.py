import os
import random

from pyray import maximize_window

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
MAX_WINDOW = (MAX_X, MAX_Y)
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 60


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Gem()
    banner.set_value(0)
    banner.set_text("Score: 0")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE - 10)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(30)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    for n in range(DEFAULT_ARTIFACTS):
        message = random.choice(["o", "*"])
        
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Gem()
        # the logic behind keeping scores
        if message == "o":
            artifact.set_value(-1)
        elif message == "*":
            artifact.set_value(1)

        artifact.set_text(message)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        artifact.set_velocity(Point(0, 5))
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()