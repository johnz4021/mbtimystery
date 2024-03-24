import pygame
import sys
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

def enter_background(background_num: str):
    background_dict: dict[str, str] = {"uchi":"resources/images/UofC-Southwest-Quad.jpg"}
    background_image_path = background_dict[background_num]
    background_image = pygame.image.load(background_image_path)
    screen.blit(background_image, (0, 0))

def enter_avatars(character_list: list[str]):
    avatar_dict: dict[str, str] = {"bossp":"resources/images/bossp.PNG",
                                   "babemax": "resources/images/babemax.PNG",
                                   "raven": "resources/images/raven.PNG",
                                   "cornelius": "resources/images/cornelius.PNG"}
    avatar_url_list = [avatar_dict[x] for x in character_list]

    for counter, avatar_path in enumerate(avatar_url_list):
        avatar = load_image(avatar_path)

        if counter % 2 == 1:
            avatar = pygame.transform.flip(avatar, True, False)

        # Adjust these values to change where the image is displayed on the screen
        image_x = (screen_width - avatar.get_width()) // (len(character_list) + 1) * (counter + 1)  # Horizontal position
        image_y = screen_height - avatar.get_height()  # Vertical position

        screen.blit(avatar, (image_x, image_y))

def draw_dialogue_box(screen, text):
    """Draws a dialogue box at the bottom of the screen with the given text and a border."""

    font = pygame.font.Font(None, 36)
    # Dialogue box dimensions and position
    box_height = 100
    box_y = screen_height - box_height

    # Border thickness
    border_thickness = 5

    # Calculate outer box dimensions for the border
    outer_box_y = box_y - border_thickness
    outer_box_height = box_height + (2 * border_thickness)

    # Render the text. True means anti-aliased text.
    text_surface = font.render(text, True, BLACK)

    # Text positioning within the dialogue box
    text_x = (screen_width - text_surface.get_width()) // 2
    text_y = outer_box_y + (outer_box_height - text_surface.get_height()) // 2

    # Draw the border box
    pygame.draw.rect(screen, PURPLE, [0, outer_box_y, screen_width, outer_box_height])

    # Draw the inner dialogue box
    pygame.draw.rect(screen, LIGHT_PINK, [border_thickness, box_y, screen_width - (2 * border_thickness), box_height])

    # Blit the text onto the screen
    screen.blit(text_surface, (text_x, text_y))


def draw_dialogue_box_with_options(screen, prompt, options, selected_option):
    """Draws a dialogue box with a prompt, multiple choice options, and a border."""
    font = pygame.font.Font(None, 36)
    box_height = 250  # Height to accommodate prompt and options
    box_y = screen_height - box_height
    border_thickness = 5  # Thickness of the border
    border_color = PURPLE  # Color of the border

    # Draw the border around the dialogue box
    pygame.draw.rect(screen, border_color,
                     [0, box_y - border_thickness, screen_width, box_height + (2 * border_thickness)])

    # Draw the dialogue box inside the border
    pygame.draw.rect(screen, LIGHT_PINK, [border_thickness, box_y, screen_width - (2 * border_thickness), box_height])

    # Draw the prompt
    prompt_surface = font.render(prompt, True, BLACK)
    screen.blit(prompt_surface, (20 + border_thickness, box_y + 10))  # Adjust for border

    # Option positioning
    option_start_y = box_y + prompt_surface.get_height() + 20  # Start below the prompt
    option_padding = 5  # Padding between options
    for index, option in enumerate(options):
        if index == selected_option:
            text_surface = font.render(option, True, BLACK, LIGHT_BLUE)
        else:
            text_surface = font.render(option, True, BLACK)

        # Calculate y position of the option
        option_y = option_start_y + index * (text_surface.get_height() + option_padding)
        screen.blit(text_surface, (20 + border_thickness, option_y))  # Adjust for border





if __name__ == "__main__":
    '''
        This code runs when this specific file is run
    '''

    #Initialization
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Mood Mystery')
    game = Game()

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
        screen.fill((255, 229, 204))  # Change the RGB values if you want a different background color

        enter_background(curr_scene.setting)
        enter_avatars(curr_scene.chara)
        #if there is still dialogue remaining
        if dialogue_progress_counter <= len(curr_dialogues) -1:
            draw_dialogue_box(screen, curr_dialogues[dialogue_progress_counter].text)
        else:
            draw_dialogue_box_with_options(screen, curr_interactive.prompt, curr_interactive.choices,selected_answer)
        # Update the display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for KEYDOWN event; KEYUP is when the key is released
            elif event.type == pygame.KEYDOWN:

                #change selected number
                if event.key == pygame.K_1:
                    selected_answer = 1
                elif event.key == pygame.K_2:
                    selected_answer = 2
                elif event.key == pygame.K_3:
                    selected_answer = 3
                elif event.key == pygame.K_4:
                    selected_answer = 4

                # Check which key was pressed
                if event.key == pygame.K_RETURN:
                    if dialogue_progress_counter <= len(curr_dialogues) - 1:
                        dialogue_progress_counter += 1
                    elif dialogue_progress_counter > len(curr_dialogues) -1:
                        #return number to the game
                        game.process_scene(selected_answer)
                        #update scene stuff
                        update_scene()
                        dialogue_progress_counter = 0 

    # Quit Pygame
    pygame.quit()
