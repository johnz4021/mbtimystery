from enum import Enum
import json
from abc import ABC


class Character(Enum):
    MC = 1
    BABEMAX = 2
    BOSSP = 3
    TUSK = 4
    LIZZI = 5
    BIRB = 6
    CORNELIUS = 7

class Text(ABC):
    """
    Base class to represent all text-based game elements.
    """
    def __init__(self, speaker: str, text: str):
        self.speaker = speaker
        self.text = text

class Dialogue(Text):
    """
    Class to represent non-interactive dialogue.
    """

    def __init__(self, speaker: str, text: str):
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
    
    def __init__(self, speaker: str, text: str, choices: dict):
        """
        Initializes the Interactive object with speaker, text (used as the prompt), and choices.

        Args:
            speaker (str): The character who is speaking.
            text (str): The prompt presented to the player.
            choices (dict): A dictionary of choices where each key is a choice label ('a', 'b', 'c', etc.)
                            and each value is a dictionary with 'response' and 'sceneReference'.
        """
        super().__init__(speaker, text)
        self.choices = {key: self.Choice(**value) for key, value in choices.items()}


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


class Game:
    """
    Main game logic class
    """

    def __init__(
        self,
        mb_score: list[int],
        ie_score: int,
        sn_score: int,
        tf_score: int,
        jp_score: int,
        scenes: dict[int:Scene],
        current_scene: int = 1,
    ):
        """
        Constructor for game logic.z

        Args:
            mb_score: Myers-Briggs score which is a list of integers consisting of ie, sn, tf, and jp scores.
            ie_score: Introverted vs. Extroverted score on scale (-10, 10) where -10 is introverted and 10 is extroverted.
            sn_score(): Introverted vs. Extroverted score on scale (-10, 10) where -10 is introverted and 10 is extroverted.
            tf_score():
            jp_score():
            scenes (list): List of scene data parsed from JSON.
            current_scene (int, optional): ID of the current scene. Defaults to 1.

        """
        self.ie_score = 0
        self.sn_score = 0
        self.tf_score = 0
        self.jp_score = 0
        self.scenes = self.load_scenes_from_json("resources\scene.json")
        self.current_scene = current_scene
        self.mb_score = [ie_score, sn_score, tf_score, jp_score]

    def load_scenes_from_json(self, json_file_path):
        """
        Loads scenes from a JSON file and returns a dictionary mapping scene_id to scene data.

        Args:
            json_file_path (str): Path to the JSON file.

        Returns:
            dict: Dictionary mapping scene_id to scene data.
        """
        with open(json_file_path, "r") as file:
            scenes = json.load(file)
        return {scene["scene_id"]: scene for scene in scenes}

    def get_scene_id(self) -> int:
        """
        Returns the current scene id number.

        Returns:
            int: Scene id number.
        """

        return 0

    def get_current_scene(self) -> Scene:
        """
        Returns the current scene

        Returns:
            Scene: The current scene.
        """
        # Fetch the scene data for the current scene ID
        scene_data = self.scenes.get(self.current_scene)
        if scene_data:
            # Initialize and return a Scene object with the fetched data
            return Scene(scene_data)
        else:
            # Handle the case where the scene ID is not found
            print(f"Scene with ID {self.current_scene} not found.")
            return None
