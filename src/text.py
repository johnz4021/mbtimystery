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
        
        Args:
            response (str): The text response of the choice.
            effect (list[int]): The effect of choosing this option, represented as a list of integers.
            sceneReference (int): The reference to the next scene after this choice is made.
        """
        
        def __init__(self, response: str, effect: list[int], sceneReference: int):
            self.response = response
            self.effect = effect
            self.sceneReference = sceneReference
    
    def __init__(self, speaker: Character, prompt: str, choices: list[Choice]):
        """
        Initializes the Interactive object with a speaker, a prompt, and choices.

        Args:
            speaker (Character): The character who is speaking.
            prompt (str): The prompt presented to the player.
            choices (List[Dict]): A list of dictionaries, each representing a choice with 'response', 'effect', and 'sceneReference'.
        """
        super().__init__(speaker, prompt)
        # Here you would transform each dict in the list to a Choice object
        self.choices = [Interactive.Choice(**choice) for choice in choices]