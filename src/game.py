import json
from abc import ABC
from scene import Scene
from src.Text import Dialogue, Interactive


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

    def load_scenes_from_json(self, json_file_path) -> dict[Scene]:
        """
        Loads scenes from a JSON file and returns a dictionary mapping scene_id to scene data.

        Args:
            json_file_path (str): Path to the JSON file.

        Returns:
            dict: Dictionary mapping scene_id to scene data.
        """
        with open(json_file_path, "r") as file:
            scenes = json.load(file)

        scenes_dict = {}
        # Iterate over each scene in the loaded list of scenes
        for scene in scenes:
            # Use the scene_id as the key and the entire scene as the value
            scenes_dict[scene["scene_id"]] = scene

        return scenes_dict

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

    def update_scores(self, player_choice: Interactive.Choice) -> None:
        """
        Updates the player's Myers-Briggs scores and its subscores with the effects of the player choice.
        """
        # This is a list of integers of effects
        effects = player_choice.effect  # ie. "[#,#,#,#]""
        if effects[0] > 0 and (effects[0] + self.ie_score > 10):
            self.ie_score = 10
        if effects[0] < 0 and (effects[0] + self.ie_score < -10):
            self.ie_score = -10
        if effects[1] > 0 and (effects[1] + self.sn_score > 10):
            self.sn_score = 10
        if effects[1] < 0 and (effects[1] + self.sn_score < -10):
            self.sn_score = -10
        if effects[2] > 0 and (effects[2] + self.ft_score > 10):
            self.ft_score = 10
        if effects[2] < 0 and (effects[2] + self.ft_score < -10):
            self.ie_score = -10
        if effects[3] > 0 and (effects[3] + self.pj_score > 10):
            self.pj_score = 10
        if effects[3] < 0 and (effects[3] + self.pj_score < -10):
            self.pj_score = -10

    # NOTE: This method may be the culprit of issues
    def process_scene(self, player_decision: int) -> None:
        """
        Updates the current scene in the game based on the player decision (usually 1-4). Updates the player scores with the effect of the choice and then changes the scene to the new scene of the choice reference.

        Args:
            player_decision (int): The number the player chooses from the list of choices from the current scene's interactive. This determines the effeect and reference scene id (ie. the new scene).
        """
        # the choice the player chooses in the current scene (Choice object)
        player_choice = self.current_scene.interactive.choices[player_decision - 1]
        self.update_scores(player_choice)
        # change the current scene to the new scene
        self.current_scene = self.scenes.get(player_choice.scene_reference)
