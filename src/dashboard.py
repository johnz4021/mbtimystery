import sys
from game import Game
import pygame

class MyersBriggsDisplay:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Detective Incognito Revealed!")
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.running = True

    def getMBTI(self) -> str:
        result = ''
        mbti = game.mb_score
        
        # Introversion (I) or Extroversion (E)
        if mbti[0] > 0:
            result += "E"
        else:
            result += "I"
        
        # Sensing (S) or Intuition (N)
        if mbti[1] > 0:
            result += "N"
        else:
            result += "S"
        
        # Thinking (T) or Feeling (F)
        if mbti[2] > 0:
            result += "T"
        else:
            result += "F"
        
        # Judging (J) or Perceiving (P)
        if mbti[3] > 0:
            result += "J"
        else:
            result += "P"
        
        return result
            
    def draw_spectrum(self, position, score, text, color):
        # Gradient background for spectrum
        start_color = (68, 85, 90)  # Dark shade
        end_color = color  # Bright color for the spectrum
        for i, ratio in enumerate(range(100)):
            pygame.draw.line(self.screen, 
                             [start_color[j] + ((float(i) / 100) * (end_color[j] - start_color[j])) for j in range(3)],
                             (100, position + ratio), (700, position + ratio), 1)

        # Score Indicator
        pygame.draw.circle(self.screen, (0, 255, 0), (int(400 + (score * 30)), position + 50), 15)
        score_text = self.font.render(f"{text}: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, position - 10))

    def run(self):
        background_color = (25, 20, 20)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(background_color)
            mbti_result = self.getMBTI()
            
            title_text = self.font.render("Detective Incognito Revealed!", True, (0, 206, 209))
            self.screen.blit(title_text, (200, 20))

            # Drawing spectrums with different colors
            self.draw_spectrum(100, self.game.ie_score, "Introverted - Extroverted", (255, 99, 71))
            self.draw_spectrum(200, self.game.sn_score, "Sensing - Intuition", (123, 104, 238))
            self.draw_spectrum(300, self.game.ft_score, "Thinking - Feeling", (60, 179, 113))
            self.draw_spectrum(400, self.game.pj_score, "Judging - Perceiving", (255, 165, 0))
            
            # Display MBTI result in large text at the bottom
            mbti_font = pygame.font.SysFont('Comic Sans MS', 48)  # Larger font size for MBTI result
            result_text = mbti_font.render(mbti_result, True, (255, 215, 0))  # Gold color for emphasis
            result_rect = result_text.get_rect(center=(400, 550))  # Positioning at the bottom center
            self.screen.blit(result_text, result_rect)

            pygame.display.flip()

# Example usage
if __name__ == "__main__":
    game = Game(ie_score=5, sn_score=-3, tf_score=2, jp_score=-7, name="Detective")
    mb_display = MyersBriggsDisplay(game)
    mb_display.run()