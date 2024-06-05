class BoardInterface:

    def reset_board(self):
        """
        Reset the board to its initial state with empty cells.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def fill_grid(self):
        """
        Fill the board with a valid Sudoku solution.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def remove_numbers(self, difficulty):
        """
        Remove numbers from the board based on the difficulty level to create the puzzle.

        Args:
            difficulty (int): The number of cells to remove based on difficulty.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def get_values(self):
        """
        Get the current values of the board.

        Returns:
            list of list of int: 2D list representing the current state of the board.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def set_values(self, values):
        """
        Set the values of the board.

        Args:
            values (list of list of int): 2D list representing the values to set on the board.
        """
        raise NotImplementedError("This method must be overridden by subclasses")