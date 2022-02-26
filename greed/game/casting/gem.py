from game.casting.actor import Actor

class Gem(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _earn_point (int): the player touches a gem they earn a point
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._earn_point = 1
    
    def set_earn_point(self, earn_point):
        """Set the points for artifacts.
        Args:
            value (int): The given point value."""
        self._earn_point = earn_point

    def get_earn_point(self):
        """gets the points value of Artifact.
        Returns:
            value (int): The artifact's point value."""
        return self._earn_point