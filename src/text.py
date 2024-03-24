from abc import ABC
from character import Character

class Text(ABC):
    """
    Base class to represent all text-based game elements.
    """
    def __init__(self, speaker: Character, text: str):
        self.speaker = speaker
        self.text = text

class Dialogue(Text):
    """
    Class to represent non-interactive dialogue.
    """

    def __init__(self, speaker: Character, text: str):
        super().__init__(speaker, text)


class Interactive(Text):
    """
    Class to represent interactive, choice-based dialogue.
    """

    class Choice:
        """
        Class to represent a single choice in an interactive dialogue.
        """
        
        def __init__(self, response: str, sceneReference: int):
            self.response = response
            self.sceneReference = sceneReference
    
    def __init__(self, speaker: Character, text: str, choices: dict):
        """
        Initializes the Interactive object with speaker, text (used as the prompt), and choices.

        Args:
            speaker (Character): The character who is speaking.
            text (str): The prompt presented to the player.
            choices (dict): A dictionary of choices where each key is a choice label ('a', 'b', 'c', etc.)
                            and each value is a dictionary with 'response' and 'sceneReference'.
        """
        super().__init__(speaker, text)
        self.choices = {key: self.Choice(**value) for key, value in choices.items()}