from enum import Enum

class Speaker(Enum):
    MC = 1
    BABEMAX = 2
    BOSSP = 3
    
    
class Dialogue:
    """
    Class to represent non-interactive dialogue
    """
    
    def __init__(
        self,
        speaker: Speaker,
        test: str
    ):
        pass

class Interactive:
    """
    Class to represent interactive, choice-based dialogue
    """
    
    def __init__(
        self,
        speaker: Speaker,
        prompt: str,
    ):
        pass
class Scene:
    """
    Class to represent dialogue and interactive text
    """
    
    def __init__(
        self,
        dialogues: list[str],
        interactive_id,
        interactive,
        stat_diff,
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
        scene_number: int,
    ):
        """
        Constructor for game logic.
        
        Args:
            ie_score = 
        
        """
        self.ie_score = 0
        self.sn_score = 0
        self.tf_score = 0
        self.jp_score = 0
        self.current_scene = 1
        self.mb_score = [ie_score, sn_score, tf_score, jp_score]