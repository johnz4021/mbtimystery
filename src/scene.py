from text import Dialogue
from text import Interactive


class Scene:
    """
    Class to represent a scene, including both dialogues and an interactive section.
    """

    def __init__(
        self,
        scene_id: int,
        speakers: list[str],
        setting: str,
        dialogues: list[Dialogue],
        interactive: Interactive,
    ):
        """
        Initializes the Scene object with an ID, setting, dialogues, and an interactive section.

        Args:
            setting (str): The setting of the scene, potentially a reference to a background image.
            dialogues (List[Dialogue]): A list of Dialogue objects representing the scene's dialogues.
            interactive (Interactive): An Interactive object representing the scene's choice-based interactive segment.
        """
        self._scene_id = scene_id
        self._speakers = speakers
        self._setting = setting
        self._dialogues = dialogues
        self._interactive = interactive

    @property
    def scene_id(self) -> int:
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value: int):
        self._scene_id = value

    @property
    def speakers(self) -> list[str]:
        return self._speakers

    @speakers.setter
    def speakers(self, value: list[str]):
        self._speakers = value

    @property
    def setting(self) -> str:
        return self._setting

    @setting.setter
    def setting(self, value: str):
        self._setting = value

    @property
    def dialogues(self) -> list[Dialogue]:
        return self._dialogues

    @dialogues.setter
    def dialogues(self, value: list[Dialogue]):
        self._dialogues = value

    @property
    def interactive(self) -> Interactive:
        return self._interactive

    @interactive.setter
    def interactive(self, value: Interactive):
        self._interactive = value
        
    def __str__(self):
            dialogues_str = ", ".join([str(dialogue) for dialogue in self._dialogues])
            interactive_str = str(self._interactive)
            return f"Scene ID: {self._scene_id}\nSpeakers: {', '.join(self._speakers)}\nSetting: {self._setting}\nDialogues: {dialogues_str}\nInteractive: {interactive_str}"