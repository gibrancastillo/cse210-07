from game.casting.actor import Actor
from game.shared.point import Point

class Gem(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__() 
        self._message = "" 
        self._value = 0
    
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The artifact's message.
        """
        return self._message

    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given messasge.
        """
        self._message = message

    def set_value(self, value):
        """Set the points for artifacts.
        Args:
            value (int): The given point value."""
        self._value = value

    def get_value(self):
        """gets the points value of Artifact.
        Returns:
            value (int): The artifact's point value."""
        return self._value