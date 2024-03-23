import pygame
import sys

screen_width = 800
screen_height = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_PINK = (255, 204, 255)
PURPLE = (178, 102, 255)  # Color for the border

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


if __name__ == "__main__":
    '''
        This code runs when this specific file is run
    '''

    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Mood Mystery')


    #SELECTED INTEGER ANSWER
    answer = 0

    # Main game loop
    running = True
    while running:
        # Fill the screen with a color to clear it
        screen.fill((255, 229, 204))  # Change the RGB values if you want a different background color

        enter_background("uchi")
        enter_avatars(["bossp", "babemax"])
        draw_dialogue_box(screen, "This is a sample dialogue box.")

        # Update the display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for KEYDOWN event; KEYUP is when the key is released
            elif event.type == pygame.KEYDOWN:
                # Check which key was pressed
                if event.key == pygame.K_1:
                    answer = 1
                    print("The '1' key was pressed.")
                elif event.key == pygame.K_2:
                    answer = 2
                    print("The '2' key was pressed.")
                elif event.key == pygame.K_3:
                    answer = 3
                    print("The '3' key was pressed.")
                elif event.key == pygame.K_4:
                    answer = 4
                    print("The '4' key was pressed.")
                elif event.key == pygame.K_RETURN:
                    print("The 'Return' key was pressed.")

    # Quit Pygame
    pygame.quit()
