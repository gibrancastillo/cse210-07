import random
from game.shared.point import Point
from game.shared.color import Color
from game.casting.gem import Gem

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        score = cast.get_first_actor("scores")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                points = banner.get_value() + artifact.get_value()
                banner.set_value(points)
                banner.set_text(f"Score: {points}")

                # Checks to add the banner with the respective color and points
                if artifact.get_value() >= 1:
                    score_kept = artifact.get_value()
                    score.set_color(Color(0, 255, 0))
                    score.set_text(f"+{score_kept} Points")
                else:    
                    score_kept = str(artifact.get_value())
                    score.set_color(Color(255, 0, 0))
                    if artifact.get_value() == 0:
                        score.set_color(Color(211, 211, 211))
                    score.set_text(f"{score_kept} Points")

                cast.remove_actor("artifacts", artifact)
                message = random.choice(["o", "*"])
                columns = (self._video_service.get_height() / self._video_service.get_cell_size())
                rows = (self._video_service.get_width() / self._video_service.get_cell_size())
                x = random.randint(1, columns - 1)
                y = random.randint(1, rows - 1)
                position = Point(x, y)
                cell_size = self._video_service.get_cell_size()
                position = position.scale(cell_size)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
        
                another_artifact = Gem()
                if message == "o":
                    another_artifact.set_value(-1)
                elif message == "*":
                    another_artifact.set_value(1)
                elif message == "?":
                    another_artifact.set_value(random.randint(-3, 3))
                another_artifact.set_text(message)
                another_artifact.set_font_size(self._video_service.get_cell_size())
                another_artifact.set_color(color)
                another_artifact.set_position(position)
                another_artifact.set_message(message)
                another_artifact.set_velocity(Point(0, 5))
                cast.add_actor("artifacts", another_artifact)
            position = artifact.get_position()
            max_x = self._video_service.get_width()
            max_y = self._video_service.get_height()
            artifact.move_next(max_x, max_y)    
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()