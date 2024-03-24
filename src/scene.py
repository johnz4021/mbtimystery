from text import Dialogue
from text import Interactive

class Scene:
    """
    Class to represent a scene, including both dialogues and an interactive section.
    """

    def __init__(self, scene_id: int, setting: str, dialogues: list[Dialogue], interactive: Interactive):
        """
        Initializes the Scene object with an ID, setting, dialogues, and an interactive section.

        Args:
            scene_id (int): Unique identifier for the scene.
            setting (str): The setting of the scene, potentially a reference to a background image.
            dialogues (List[Dialogue]): A list of Dialogue objects representing the scene's dialogues.
            interactive (Interactive): An Interactive object representing the scene's choice-based interactive segment.
        """
        self.scene_id = scene_id
        self.setting = setting
        self.dialogues = dialogues
        self.interactive = interactive