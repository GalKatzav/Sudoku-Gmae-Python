class CellInterface:
    def set_value(self, value):
        """
        Set the value of the cell and update its display.

        Args:
            value (int): The value to set.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def draw(self, surface, font, colors):
        """
        Draw the cell on the given surface.

        Args:
            surface (pygame.Surface): The surface where the cell will be drawn.
            font (pygame.font.Font): The font to be used for drawing the cell value.
            colors (dict): Dictionary containing colors for drawing the cell.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def select(self):
        """
        Highlight the cell to indicate it is selected.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def deselect(self):
        """
        Remove the highlight to indicate the cell is deselected.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def is_fixed(self):
        """
        Check if the cell value is fixed.

        Returns:
            bool: True if the cell value is fixed, False otherwise.
        """
        raise NotImplementedError("This method must be overridden by subclasses")
