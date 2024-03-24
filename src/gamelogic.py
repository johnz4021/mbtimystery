from enum import Enum
import json

class Character(Enum):
    MC = 1
    BABEMAX = 2
    BOSSP = 3
    TUSK = 4
    LIZZI = 5
    BIRB = 6
    CORNELIUS = 7
    
    
class Dialogue:
    """
    Class to represent non-interactive dialogue
    """
    
    def __init__(
        self,
        speaker: Character,
        test: str
    ):
        pass

class Interactive:
    """
    Class to represent interactive, choice-based dialogue
    """
    
    def __init__(
        self,
        speaker: Character,
        prompt: str,
    ):
        pass
class Scene:
    """
    Class to represent dialogue and interactive text.
    """
    
    def __init__(
        self,
        current_Character: 'Character',
        dialogues: list['Dialogue'],
        interactive_id: int,
        interactive: 'Interactive',
        stat_diff: list[int],
    ):
        pass



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
        scenes: dict[int: Scene],
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
        with open(json_file_path, 'r') as file:
            scenes = json.load(file)
        return {scene['scene_id']: scene for scene in scenes}
    
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