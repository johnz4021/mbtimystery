class Dialogue:
    """
    Class to represent non-interactive dialogue.
    """

    def __init__(self, speaker: str, text: str):
        self._speaker = speaker
        self._text = text

    @property
    def speaker(self) -> str:
        return self._speaker  # Return the backing field

    @speaker.setter
    def speaker(self, value: str):
        self._speaker = value  # Modify the backing field

    @property
    def text(self) -> str:
        return self._text  # Return the backing field

    @text.setter
    def text(self, value: str):
        self._text = value  # Modify the backing field


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
            self._response = response
            self._effect = effect
            self._scene_reference = scene_reference

        @property
        def response(self) -> str:
            return self._response

        @response.setter
        def response(self, value: str):
            self._response = value

        @property
        def scene_reference(self) -> int:
            return self._scene_reference

        @scene_reference.setter
        def scene_reference(self, value: int):
            self._scene_reference = value

        @property
        def effect(self) -> list[int]:
            return self._effect

        @effect.setter
        def effect(self, value: list[int]):
            self._effect = value
            
        def __str__(self):
            effect_str = ", ".join(map(str, self._effect))
            return f"Response: {self._response}, Effect: [{effect_str}], Scene Reference: {self._scene_reference}"

    def __init__(self, speaker: str, prompt: str, choices: list[dict]):
        """
        Initializes the Interactive object with a speaker, a prompt, and choices.

        Args:
            speaker (str): The character who is speaking.
            prompt (str): The prompt presented to the player.
            choices (list[dict]): A list of dictionaries, each representing a choice with 'response', 'effect', and 'scene_reference'.
        """
        self._speaker = speaker
        self._prompt = prompt
        # Initialize the choices attribute as an empty list
        self._choices = choices
        # for choice in choices:
        #     # For each choice in the list, unpack its keys and values as arguments to the Choice class constructor
        #     choice_obj = Interactive.Choice(
        #         response=choice["response"],
        #         effect=choice["effect"],
        #         scene_reference=choice["scene_reference"],
        #     )
        #     # Append the newly created Choice object to the choices attribute
        #     self.choices.append(choice_obj)

    @property
    def choices(self) -> list[Choice]:
        return self._choices

    @choices.setter
    def choices(self, value: list):
        self._choices = value

    @property
    def speaker(self) -> str:
        return self._speaker

    @speaker.setter
    def speaker(self, value: str):
        self._speaker = value

    @property
    def prompt(self) -> str:
        return self._prompt

    @prompt.setter
    def prompt(self, value: str):
        self._prompt = value
