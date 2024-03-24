from text import Dialogue
from text import Interactive

class Scene:
    """
    Class to represent a scene, including both dialogues and an interactive section.
    """

    def __init__(self, speakers:list[str], setting: str, dialogues: list[Dialogue], interactive: Interactive):
        """
        Initializes the Scene object with an ID, setting, dialogues, and an interactive section.

        Args:
            setting (str): The setting of the scene, potentially a reference to a background image.
            dialogues (List[Dialogue]): A list of Dialogue objects representing the scene's dialogues.
            interactive (Interactive): An Interactive object representing the scene's choice-based interactive segment.
        """
        self.speakers = speakers
        self.setting = setting
        self.dialogues = dialogues
        self.interactive = interactive
    @property
    def speakers(self) -> list[str]:
        return self.speakers
    @property
    def setting(self) -> str:
        return self.setting
    
    @property
    def dialogues(self) -> list[Dialogue]:
        return self.dialogues
    
    @property
    def interactive(self) -> Interactive:
        return self.interactive