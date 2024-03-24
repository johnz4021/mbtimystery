class Dialogue:
    """
    Class to represent non-interactive dialogue.
    """

    def __init__(self, speaker: str, text: str):
        self.speaker = speaker
        self.text = text

    @property
    def speaker(self) -> str:
        return self.speaker

    @property
    def text(self) -> str:
        return self.text

    @speaker.setter
    def speaker(self, value: str):
        self._speaker = value  # Allow setting the speaker

    @text.setter
    def text(self, value: str):
        self._text = value  # Allow setting the text


class Interactive:
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

        @response.setter
        def response(self, value: str):
            self._response = value

        @property
        def scene_reference(self) -> int:
            return self.scene_reference

        @scene_reference.setter
        def scene_reference(self, value: int):
            self._sceneReference = value

        @property
        def effect(self) -> list[int]:
            return self.effect

        @effect.setter
        def effect(self, value: list[int]):
            self._effect = value

    def __init__(self, speaker: str, prompt: str, choices: list[dict]):
        """
        Initializes the Interactive object with a speaker, a prompt, and choices.

        Args:
            speaker (str): The character who is speaking.
            prompt (str): The prompt presented to the player.
            choices (list[dict]): A list of dictionaries, each representing a choice with 'response', 'effect', and 'sceneReference'.
        """
        self.speaker = speaker
        self.prompt = prompt
        # Initialize the choices attribute as an empty list
        self.choices = choices
        # for choice in choices:
        #     # For each choice in the list, unpack its keys and values as arguments to the Choice class constructor
        #     choice_obj = Interactive.Choice(
        #         response=choice["response"],
        #         effect=choice["effect"],
        #         scene_reference=choice["sceneReference"],
        #     )
        #     # Append the newly created Choice object to the choices attribute
        #     self.choices.append(choice_obj)

    @property
    def choices(self) -> list[Choice]:
        return self.choices

    @choices.setter
    def choices(self, value: list):
        self._choices = value

    @property
    def speaker(self) -> str:
        return self.speaker

    @speaker.setter
    def speaker(self, value: str):
        self._speaker = value

    @property
    def prompt(self) -> str:
        return self.prompt

    @prompt.setter
    def prompt(self, value: str):
        self._prompt = value
