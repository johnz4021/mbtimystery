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
            name (str): Name of the Main Character (defaults to 'MC')
            mb_score (list[int]): Myers-Briggs score, a list of integers consisting of ie, sn, ft, and pj scores.
            ie_score (int): Introverted vs. Extroverted score on a scale of (-10, 10), where -10 is more introverted and 10 is more extroverted.
            sn_score (int): Sensing vs. Intuition score on a scale of (-10, 10), where -10 is more Sensing and 10 is more Intuition.
            ft_score (int): Feeling vs. Thinking score on a scale of (-10, 10), where -10 is more Feeling and 10 is more Thinking.
            pj_score (int): Perceiving vs. Judging score on a scale of (-10, 10), where -10 is more Perceiving and 10 is more Judging .
            scenes (dict[int, Scene]): Dictionary mapping scene IDs to Scene objects, representing all possible scenes in the game.
            current_scene (int, optional): ID of the current scene. Defaults to 1.

        """
        self.name = "MC"
        self.ie_score = 0
        self.sn_score = 0
        self.ft_score = 0
        self.pj_score = 0
        self.scenes = self.load_scenes_from_json("resources\scene.json")
        self.current_scene = current_scene
        self.mb_score = [ie_score, sn_score, tf_score, jp_score]

    # TODO: SET NAME AT THE BEGINNING OF THE GAME
    @property
    def name(self) -> str:
        """
        Returns the name of the main character (MC).
        """
        return self.name

    @property
    def ie_score(self) -> int:
        return self.ie_score

    @property
    def sn_score(self) -> int:
        return self.sn_score

    @property
    def ft_score(self) -> int:
        return self.ft_score

    @property
    def pj_score(self) -> int:
        return self.pj_score

    def load_scenes_from_json(self, json_file_path) -> dict[int: Scene]:
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
    
    def change_current_scene(self, player_decision: int) -> None:
        """
        Updates the current scene in the game based on the player decision (usually 1-4).

        Args:
            choice_id (_type_): The number the player chooses from the list of choices from the current scene's interactive. This determines the reference scene id (ie. the new scene).
        """