from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__() # To inherit Actor's attributes
        self._message = "" # "You found kitten!"
    
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