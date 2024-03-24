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
            effect (list[int]): The Myers-Briggs score effect of choosing this option, represented as a list of integers corresponding to [ie, sn, ft, pj].
            scene_reference (int): The reference to the next scene after this choice is made.
        """

        def __init__(self, response: str, effect: list[int], scene_reference: int):
            self.response = response
            self.effect = effect
            self.sceneReference = scene_reference
                
        @property
        def response(self) -> str:
            return self.response
        
        @property
        def scene_reference(self) -> int:
            return self.scene_reference
        
        @property
        def effect(self) -> list[int]:
            return self.effect

    def __init__(self, speaker: Character, prompt: str, choices: list[dict]):
        """
        Initializes the Interactive object with a speaker, a prompt, and choices.

        Args:
            speaker (Character): The character who is speaking.
            prompt (str): The prompt presented to the player.
            choices (list[dict]): A list of dictionaries, each representing a choice with 'response', 'effect', and 'sceneReference'.
        """
        super().__init__(speaker, prompt)
        # Initialize the choices attribute as an empty list
        self.choices = []
        for choice in choices:
            # For each choice in the list, unpack its keys and values as arguments to the Choice class constructor
            choice_obj = Interactive.Choice(
                response=choice["response"],
                effect=choice["effect"],
                scene_reference=choice["sceneReference"],
            )
            # Append the newly created Choice object to the choices attribute
            self.choices.append(choice_obj)

    @property
    def choices(self) -> list[Choice]:
        return self.choices
