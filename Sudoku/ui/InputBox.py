import pygame  # Import the Pygame library

class InputBox:
    def __init__(self, x, y, w, h, font, text=''):
        """
        Initialize the InputBox.
        :param x: The x-coordinate of the input box
        :param y: The y-coordinate of the input box
        :param w: The width of the input box
        :param h: The height of the input box
        :param font: The font used for rendering text
        :param text: The initial text of the input box (default is empty)
        """
        self.rect = pygame.Rect(x, y, w, h)  # Create a rectangle for the input box
        self.color = pygame.Color('lightskyblue3')  # Set the initial color of the input box
        self.text = text  # Set the initial text
        self.font = font  # Assign the passed font
        self.txt_surface = self.font.render(text, True, self.color)  # Render the initial text surface
        self.active = False  # The input box is initially inactive

    def handle_event(self, event):
        """
        Handle events related to the input box.
        :param event: The event to handle
        :return: The text if Enter key is pressed, None otherwise
        """
        if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button down events
            if self.rect.collidepoint(event.pos):  # Check if the mouse click is within the input box
                self.active = not self.active  # Toggle the active state
            else:
                self.active = False  # Deactivate the input box if clicked outside
            # Change color based on active state
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:  # Check for key down events
            if self.active:  # Only handle events if the input box is active
                if event.key == pygame.K_RETURN:  # If Enter key is pressed
                    return self.text  # Return the current text
                elif event.key == pygame.K_BACKSPACE:  # If Backspace key is pressed
                    self.text = self.text[:-1]  # Remove the last character
                else:
                    self.text += event.unicode  # Add the character to the text
                # Render the updated text surface
                self.txt_surface = self.font.render(self.text, True, self.color)
        return None  # Return None if no text is submitted

    def draw(self, screen):
        """
        Draw the input box on the screen.
        :param screen: The screen to draw on
        """
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))  # Draw the text surface
        pygame.draw.rect(screen, self.color, self.rect, 2)  # Draw the input box rectangle
