import pygame  # Import the Pygame library

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        """
        Initialize the Button.
        :param text: The text to display on the button
        :param pos: The position of the button (x, y)
        :param font: The font to use for the button text
        :param bg: The background color of the button (default is black)
        :param feedback: The feedback text when the button is clicked (default is the same as the button text)
        """
        self.x, self.y = pos  # Set the x and y coordinates of the button
        self.font = font  # Set the font for the button text
        if feedback == "":  # If no feedback text is provided
            self.feedback = text  # Use the button text as the feedback text
        else:
            self.feedback = feedback  # Use the provided feedback text
        self.change_text(text, bg)  # Change the button text

    def change_text(self, text, bg="black"):
        """
        Change the text of the button.
        :param text: The new text to display on the button
        :param bg: The background color of the button (default is black)
        """
        self.text = self.font.render(text, True, pygame.Color("White"))  # Render the button text
        self.size = self.text.get_size()  # Get the size of the rendered text
        self.surface = pygame.Surface(self.size)  # Create a surface for the button
        self.surface.fill(bg)  # Fill the surface with the background color
        self.surface.blit(self.text, (0, 0))  # Blit the text onto the surface
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])  # Create a rectangle for the button

    def show(self, screen):
        """
        Display the button on the screen.
        :param screen: The screen to display the button on
        """
        screen.blit(self.surface, (self.x, self.y))  # Blit the button surface onto the screen

    def click(self, event):
        """
        Check if the button is clicked.
        :param event: The Pygame event
        :return: True if the button is clicked, False otherwise
        """
        x, y = pygame.mouse.get_pos()  # Get the current mouse position
        if self.rect.collidepoint(x, y):  # Check if the mouse position is within the button rectangle
            return True  # Return True if the button is clicked
        return False  # Return False if the button is not clicked
