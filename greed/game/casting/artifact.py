from game.casting.actor import Actor

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _point (int): the player touches a gem they earn a point, a rock they lose a point
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._point = 1
    
    def set_point(self, point):
        """Set the points for artifacts.
        Args:
            value (int): The given point value."""
        self._point = point

    def get_point(self):
        """gets the points value of Artifact.
        Returns:
            value (int): The artifact's point value."""
        return self._point