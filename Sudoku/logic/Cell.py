import pygame  # Import the Pygame library

# Define colors
BLACK = (0, 0, 0)  # RGB color for black
WHITE = (255, 255, 255)  # RGB color for white
BLUE = (0, 0, 255)  # RGB color for blue
RED = (255, 0, 0)  # RGB color for red


class Cell:
    def __init__(self, row, col, size, value=0, fixed=False):
        """
        Initialize the Cell.
        :param row: The row index of the cell
        :param col: The column index of the cell
        :param size: The size of the cell
        :param value: The initial value of the cell (default is 0)
        :param fixed: Boolean indicating if the cell value is fixed (default is False)
        """
        try:
            self.row = row  # Assign the row index to the cell
            self.col = col  # Assign the column index to the cell
            self.size = size  # Assign the size to the cell
            self.value = value  # Initialize value from parameter
            self.fixed = fixed  # Initialize fixed status from parameter
            self.selected = False  # Initialize the selected status as False
            self.color = BLACK  # Default text color
        except Exception as e:
            print(f"Error initializing the cell: {e}")

    def set_value(self, value, color=BLACK):
        """
        Set the value of the cell.
        :param value: The value to be set in the cell
        :param color: The color of the value text
        """
        try:
            self.value = value  # Assign the new value to the cell
            self.color = color  # Assign the color to the cell text
        except Exception as e:
            print(f"Error setting cell value: {e}")

    def set_color(self, color):
        """
        Set the color of the cell's value.
        :param color: The color to be set
        """
        try:
            self.color = color  # Assign the color to the cell text
        except Exception as e:
            print(f"Error setting cell color: {e}")

    def draw(self, surface, font):
        """
        Draw the cell on the given surface.
        :param surface: The surface where the cell will be drawn
        :param font: The font to be used for drawing the cell value
        """
        try:
            x1 = self.col * self.size  # Calculate the x-coordinate of the top-left corner
            y1 = self.row * self.size  # Calculate the y-coordinate of the top-left corner
            rect = (x1, y1, self.size, self.size)  # Define the rectangle area
            pygame.draw.rect(surface, WHITE, rect)  # Draw the rectangle with the background color
            pygame.draw.rect(surface, BLACK, rect, 1)  # Draw the rectangle outline

            if self.value != 0:  # If the cell value is not zero
                value_surf = font.render(str(self.value), True, self.color)  # Render the text with the assigned color
                value_rect = value_surf.get_rect(center=(x1 + self.size // 2, y1 + self.size // 2))  # Center the text in the cell
                surface.blit(value_surf, value_rect)  # Draw the text on the surface

            if self.selected:  # If the cell is selected
                pygame.draw.rect(surface, BLUE, rect, 3)  # Draw a highlight border
        except Exception as e:
            print(f"Error drawing the cell: {e}")

    def select(self):
        """
        Select the cell.
        """
        try:
            self.selected = True  # Set the selected status to True
        except Exception as e:
            print(f"Error selecting the cell: {e}")

    def deselect(self):
        """
        Deselect the cell.
        """
        try:
            self.selected = False  # Set the selected status to False
        except Exception as e:
            print(f"Error deselecting the cell: {e}")

    def is_fixed(self):
        """
        Check if the cell value is fixed.
        :return: True if the cell value is fixed, False otherwise
        """
        return self.fixed  # Return the fixed status of the cell
