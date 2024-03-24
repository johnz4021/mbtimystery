import json
from abc import ABC
from scene import Scene
from text import Dialogue, Interactive


class Game:
    """
    Main game logic class
    """

    def __init__(
        self,
        ie_score: int = 0,
        sn_score: int = 0,
        tf_score: int = 0,
        jp_score: int = 0,
        name: str = "MC",
    ):
        """
        Constructor for game logic

        Args:
            ie_score (int): Introverted vs. Extroverted score on a scale of (-10, 10), where -10 is more introverted and 10 is more extroverted.
            sn_score (int, optional): Sensing vs. Intuition score on a scale of (-10, 10), where -10 is more Sensing and 10 is more Intuition.
            ft_score (int, optional): Feeling vs. Thinking score on a scale of (-10, 10), where -10 is more Feeling and 10 is more Thinking.
            pj_score (int, optional): Perceiving vs. Judging score on a scale of (-10, 10), where -10 is more Perceiving and 10 is more Judging .
            name (str, optional): Name of the Main Character (defaults to 'MC')

        """

        # scenes (dict[int, Scene]): Dictionary mapping scene IDs to Scene objects, representing all possible scenes in the game.
        self.scenes = self.load_scenes_from_json("resources/scene.json")
        self.current_scene = self.scenes[0]

        # mb_score (list[int]): Myers-Briggs score, a list of integers consisting of ie, sn, ft, and pj scores.
        self.mb_score = [ie_score, sn_score, tf_score, jp_score]

    # TODO: SET NAME AT THE BEGINNING OF THE GAME
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def ie_score(self) -> int:
        return self._ie_score

    @ie_score.setter
    def ie_score(self, value: int):
        self._ie_score = value

    @property
    def sn_score(self) -> int:
        return self._sn_score

    @sn_score.setter
    def sn_score(self, value: int):
        self._sn_score = value

    @property
    def ft_score(self) -> int:
        return self._ft_score

    @ft_score.setter
    def ft_score(self, value: int):
        self._ft_score = value

    @property
    def pj_score(self) -> int:
        return self._pj_score

    @pj_score.setter
    def pj_score(self, value: int):
        self._pj_score = value

    @property
    def current_scene(self) -> Scene:
        return self._current_scene

    @current_scene.setter
    def current_scene(self, value: Scene):
        self._current_scene = value

    def load_scenes_from_json(self, json_file_path) -> list[Scene]:
        """
        Loads scenes from a JSON file and returns a list of fully initialized Scene objects.

        Args:
            json_file_path (str): Path to the JSON file.
        """
        with open(json_file_path, "r") as file:
            scenes_data = json.load(file)

        scenes_list = []
        
        for scene_data in scenes_data:
            # Construct Dialogue objects for each dialogue entry in the scene
            dialogues = []
            for dialogue in scene_data["dialogues"]:
                speaker = dialogue["speaker"]
                text = dialogue["text"]

                dialogues.append(Dialogue(speaker, text))

            # Construct Interactive.Choice objects for each choice in the interactive entry
            choices = []

            for choice in scene_data["interactive"]["choices"]:
                response = choice["response"]
                effect = choice["effect"]
                scene_reference = choice["sceneReference"]

                choices.append(Interactive.Choice(response, effect, scene_reference))

            # Construct the Interactive object (uses choices)
            interactive_speaker = scene_data["interactive"]["speaker"]
            interactive_prompt = scene_data["interactive"]["prompt"]

            interactive = Interactive(interactive_speaker, interactive_prompt, choices)

            # Initialize the Scene object
            scene_id = scene_data["scene_id"]
            scene_speakers = scene_data["speakers"].split(",")
            scene_setting = scene_data["setting"]

            scene = Scene(
                scene_id, scene_speakers, scene_setting, dialogues, interactive
            )

            scenes_list.append(scene)

        return scenes_list

    def get_current_scene_id(self) -> int:
        """
        Returns the current scene id number.

        Returns:
            int: Scene id number.
        """

        return self.current_scene.scene_id

    def update_scores(self, player_choice: Interactive.Choice) -> None:
        """
        Updates the player's Myers-Briggs scores and its subscores with the effects of the player choice.
        """
        # This is a list of integers of effects
        effects = player_choice.effect  # ie. "[#,#,#,#]""

        # Update ie_score
        if effects[0] > 0 and (effects[0] + self.ie_score > 10):
            self.ie_score = 10
        elif effects[0] < 0 and (effects[0] + self.ie_score < -10):
            self.ie_score = -10
        else:
            self.ie_score += effects[0]

        # Update sn_score
        if effects[1] > 0 and (effects[1] + self.sn_score > 10):
            self.sn_score = 10
        elif effects[1] < 0 and (effects[1] + self.sn_score < -10):
            self.sn_score = -10
        else:
            self.sn_score += effects[1]

        # Update ft_score
        if effects[2] > 0 and (effects[2] + self.ft_score > 10):
            self.ft_score = 10
        elif effects[2] < 0 and (effects[2] + self.ft_score < -10):
            self.ft_score = -10
        else:
            self.ft_score += effects[2]

        # Update pj_score
        if effects[3] > 0 and (effects[3] + self.pj_score > 10):
            self.pj_score = 10
        elif effects[3] < 0 and (effects[3] + self.pj_score < -10):
            self.pj_score = -10
        else:
            self.pj_score += effects[3]

    # NOTE: This method may be the culprit of issues
    def process_scene(self, player_decision: int) -> None:
        """
        Updates the current scene in the game based on the player decision (usually 1-4). Updates the player scores with the effect of the choice and then changes the scene to the new scene of the choice reference.

        Args:
            player_decision (int): The number the player chooses from the list of choices from the current scene's interactive. This determines the effect and reference scene id (ie. the new scene).
        """
        # the choice the player chooses in the current scene (Choice object)
        player_choice = self.current_scene.interactive.choices[player_decision - 1]
        self.update_scores(player_choice)
        # change the current scene to the new scene
        self.current_scene = self.scenes.get(player_choice.scene_reference)
