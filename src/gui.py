import pygame
import sys
import textwrap
from game import Game, Scene
from text import Dialogue, Interactive

screen_width = 800
screen_height = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_PINK = (255, 204, 255)
PURPLE = (178, 102, 255)  # Color for the border
LIGHT_BLUE = (173, 216, 230)  # Highlight color

def load_image(image_path):
    """Load an image from the specified file path."""
    try:
        image = pygame.image.load(image_path)
        return image
    except pygame.error as e:
        print(f'Error loading image: {e}')
        sys.exit(1)

def enter_background(background_name: str):
    background_image_path = f"resources/images/{background_name}"
    background_image = pygame.image.load(background_image_path)
    screen.blit(background_image, (0, 0))

def show_title_screen():
    title_screen = pygame.image.load("resources/images/title_screen.jpeg")
    image_x = (screen_width - title_screen.get_width()) // 2
    image_y = (screen_height - title_screen.get_height()) // 2
    screen.blit(title_screen, (image_x, image_y))

def enter_avatars(character_list: list[str]):
    avatar_dict: dict[str, str] = {"BOSSP":"resources/images/bossp.PNG",
                                   "BABEMAX": "resources/images/babemax.PNG",
                                   "RAVEN": "resources/images/raven.PNG",
                                   "CORNELIUS": "resources/images/cornelius.PNG"}

    avatar_url_list = [avatar_dict[x] for x in character_list]

    for counter, avatar_path in enumerate(avatar_url_list):
        avatar = load_image(avatar_path)

        if counter % 2 == 1:
            avatar = pygame.transform.flip(avatar, True, False)

        # Adjust these values to change where the image is displayed on the screen
        image_x = (screen_width - avatar.get_width()) // (len(character_list) + 1) * (counter + 1)  # Horizontal position
        image_y = screen_height - avatar.get_height()  # Vertical position

        screen.blit(avatar, (image_x, image_y))

def draw_text_wrapped(surface, text, pos, font, max_width, color):
    """Draws text on a surface, wrapping words to stay within a specified width."""
    words = textwrap.wrap(text, width=max_width)
    x, y = pos
    for word in words:
        word_surface = font.render(word, True, color)
        surface.blit(word_surface, (x, y))
        y += font.get_linesize()  # Move to the next line

def draw_dialogue_box(screen, text):
    """Draws a dialogue box at the bottom of the screen with the given text and a border."""

    font = pygame.font.Font(None, 25)
    # Dialogue box dimensions and position
    box_height = 100
    box_y = screen_height - box_height

    # Border thickness
    border_thickness = 5

    # Calculate outer box dimensions for the border
    outer_box_y = box_y - border_thickness
    outer_box_height = box_height + (2 * border_thickness)

    # Define colors
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    LIGHT_PINK = (255, 182, 193)

    # Maximum width for text
    max_text_width = screen_width - (2 * border_thickness) - 20  # Adjust padding as needed

    # Draw the border box
    pygame.draw.rect(screen, PURPLE, [0, outer_box_y, screen_width, outer_box_height])

    # Draw the inner dialogue box
    pygame.draw.rect(screen, LIGHT_PINK, [border_thickness, box_y, screen_width - (2 * border_thickness), box_height])

    # Text positioning within the dialogue box
    text_x = (screen_width - max_text_width) // 2  # Center the text block
    text_y = outer_box_y + (outer_box_height - box_height) // 2 + border_thickness

    # Render and blit the wrapped text onto the screen
    draw_text_wrapped(screen, text, (text_x, text_y), font, 80, BLACK)  # 60 characters, adjust as needed


def draw_text_wrapped_2(surface, text, pos, font, max_width, color, bg_color=None):
    """Draws text on a surface, wrapping words to stay within a specified width, and returns the height of the drawn text."""
    words = text.split(' ')  # Split the text by spaces to find words
    space_width, line_height = font.size(' ')  # Width of a space and the height of a line of text.
    x, initial_y = pos
    y = initial_y
    for word in words:
        word_surface = font.render(word, True, color, bg_color)
        word_width, word_height = word_surface.get_size()
        if x + word_width > max_width:
            x = pos[0]  # Reset x to start of line.
            y += line_height  # Start on new line.
        surface.blit(word_surface, (x, y))
        x += word_width + space_width  # Move x to start of next word.

    # Return the total height of the rendered text
    return y + line_height - initial_y


def draw_dialogue_box_with_options(screen, prompt, options, selected_option):
    """Draws a dialogue box with a prompt, multiple choice options, and a border."""
    font = pygame.font.Font(None, 25)
    # Define colors
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    LIGHT_PINK = (255, 182, 193)
    LIGHT_BLUE = (173, 216, 230)  # Highlight color

    box_height = 150  # Height to accommodate prompt and options
    box_y = screen_height - box_height
    border_thickness = 5  # Thickness of the border
    max_text_width = screen_width - (2 * border_thickness) - 40  # Adjust padding as needed

    # Draw the border around the dialogue box
    pygame.draw.rect(screen, PURPLE, [0, box_y - border_thickness, screen_width, box_height + (2 * border_thickness)])

    # Draw the dialogue box inside the border
    pygame.draw.rect(screen, LIGHT_PINK, [border_thickness, box_y, screen_width - (2 * border_thickness), box_height])

    # Draw the prompt with text wrapping and calculate its height
    prompt_height = draw_text_wrapped_2(screen, prompt, (20 + border_thickness, box_y + 10), font, screen_width - 40,
                                      BLACK) + 20  # Extra spacing after the prompt

    # Option positioning starts below the prompt
    option_start_y = box_y + 10 + prompt_height  # Adjusted for prompt height

    option_padding = 20  # Increased padding between options for clarity
    for index, option in enumerate(options):
        option_bg_color = LIGHT_BLUE if index + 1 == selected_option else None
        option_height = draw_text_wrapped_2(screen, option, (20 + border_thickness, option_start_y), font,
                                          screen_width - 40, BLACK, option_bg_color)
        option_start_y += option_height + option_padding

if __name__ == "__main__":
    '''
        This code runs when this specific file is run
    '''

    #Initialization
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Mood Mystery')
    game = Game()

    #title screen check
    title_screen_check = 0

    def update_scene():
        scene = game.current_scene
        dialogues = scene.dialogues
        interactive = scene.interactive
        return scene, dialogues, interactive

    #Variable scene content
    curr_scene, curr_dialogues, curr_interactive = update_scene()
    #Counters
    dialogue_progress_counter = 0

    #Selected integer answer
    selected_answer = 1

    # Main game loop
    running = True
    while running:
        # Fill the screen with a color to clear it
        screen.fill(WHITE)  # Change the RGB values if you want a different background color

        if title_screen_check == 0:
            show_title_screen()
            pygame.display.flip()
        else:
            enter_background(curr_scene.setting)
            enter_avatars(curr_scene.speakers)
            #if there is still dialogue remaining
            if dialogue_progress_counter <= len(curr_dialogues) -1:
                draw_dialogue_box(screen, curr_dialogues[dialogue_progress_counter].text)
            else:
                choices_list = curr_interactive.choices
                text_list = [choices_list[x].response for x in range(len(choices_list))]
                draw_dialogue_box_with_options(screen, curr_interactive.prompt, text_list,selected_answer)
            # Update the display
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for KEYDOWN event; KEYUP is when the key is released
            elif event.type == pygame.KEYDOWN:
                #change selected number
                if event.key == pygame.K_1 and len(curr_interactive.choices) >= 1:
                    selected_answer = 1
                elif event.key == pygame.K_2 and len(curr_interactive.choices) >= 2:
                    selected_answer = 2
                elif event.key == pygame.K_3 and len(curr_interactive.choices) >= 3:
                    selected_answer = 3

                # Check which key was pressed
                if event.key == pygame.K_RETURN:
                    if title_screen_check == 0:
                        title_screen_check += 1
                    elif dialogue_progress_counter <= len(curr_dialogues) - 1:
                        dialogue_progress_counter += 1
                    elif dialogue_progress_counter > len(curr_dialogues) -1:
                        #return number to the game
                        game.process_scene(selected_answer)
                        #update scene stuff
                        update_scene()
                        dialogue_progress_counter = 0 

    # Quit Pygame
    pygame.quit()
