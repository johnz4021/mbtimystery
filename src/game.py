
import json
from abc import ABC
from scene import Scene

class Game:
    """
    Main game logic class
    """

    def __init__(
        self,
        name: str,
        mb_score: list[int],
        ie_score: int,
        sn_score: int,
        tf_score: int,
        jp_score: int,
        scenes: dict[int:Scene],
        current_scene: int = 1,
    ):
        """
        Constructor for game logic

        Args:
            mc_name (str): Name of the Main Character (defaults to 'MC')
            mb_score (list[int]): Myers-Briggs score, a list of integers consisting of ie, sn, tf, and jp scores.
            ie_score (int): Introverted vs. Extroverted score on a scale of (-10, 10), where -10 is fully introverted and 10 is fully extroverted.
            sn_score (int): Sensing vs. Intuition score on a scale of (-10, 10), where -10 leans towards Sensing and 10 towards Intuition.
            tf_score (int): Thinking vs. Feeling score on a scale of (-10, 10), where -10 is more Thinking-oriented and 10 is more Feeling-oriented.
            jp_score (int): Judging vs. Perceiving score on a scale of (-10, 10), where -10 favors Judging and 10 favors Perceiving.
            scenes (dict[int, Scene]): Dictionary mapping scene IDs to Scene objects, representing all possible scenes in the game.
            current_scene (int, optional): ID of the current scene. Defaults to 1.

        """
        self.name = "MC"
        self.ie_score = 0
        self.sn_score = 0
        self.tf_score = 0
        self.jp_score = 0
        self.scenes = self.load_scenes_from_json("resources\scene.json")
        self.current_scene = current_scene
        self.mb_score = [ie_score, sn_score, tf_score, jp_score]
    
    @property
    def name(self) -> str:
        """
        Returns the name of the main character (MC).
        """
        return self.name

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

    def get_current_scene_id(self) -> int:
        """
        Returns the current scene id number.

        Returns:
            int: Scene id number.
        """

        return self.current_scene.scene_id

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
