import pygame
import sys

if __name__ == "__main__":
    '''
        This code runs when this specific file is run
    '''

    pygame.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Mood Mystery')


    def load_image(image_path):
        """Load an image from the specified file path."""
        try:
            image = pygame.image.load(image_path)
            return image
        except pygame.error as e:
            print(f'Error loading image: {e}')
            sys.exit(1)

    def draw_dialogue_box(screen, text):
        """Draws a dialogue box at the bottom of the screen with the given text."""
        # Dialogue box dimensions and position
        box_height = 100
        box_y = screen_height - box_height

        # Render the text. True means anti-aliased text.
        # Black text on a white background
        text_surface = font.render(text, True, BLACK, GRAY)

        # Text positioning within the dialogue box
        text_x = (screen_width - text_surface.get_width()) // 2
        text_y = box_y + (box_height - text_surface.get_height()) // 2

        # Draw the dialogue box
        pygame.draw.rect(screen, GRAY, [0, box_y, screen_width, box_height])

        # Blit the text onto the screen
        screen.blit(text_surface, (text_x, text_y))


    image_path = "/Users/johnzhang/PycharmProjects/moodmystery/download.png"
    image = load_image(image_path)

    # Adjust these values to change where the image is displayed on the screen
    image_x = (screen_width - image.get_width()) // 2  # Horizontal position
    image_y = screen_height - image.get_height()  # Vertical position

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color to clear it
        screen.fill((255, 229, 204))  # Change the RGB values if you want a different background color

        # Blit the image onto the screen at the specified position
        screen.blit(image, (image_x, image_y))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
