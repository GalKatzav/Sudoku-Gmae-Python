class SolverInterface:

    def is_valid(self, board, num, position):
        """
        Check if a number can be placed in a specific position.

        Args:
            board (list of list of int): 2D list representing the Sudoku board.
            num (int): Number to place.
            position (tuple of int): Tuple representing the row and column.

        Returns:
            bool: True if the number can be placed, False otherwise.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def find_empty(self, board):
        """
        Find an empty cell in the Sudoku board.

        Args:
            board (list of list of int): 2D list representing the Sudoku board.

        Returns:
            tuple of int or None: Tuple representing the row and column of the empty cell, or None if no empty cells.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def is_valid_solution(self, board):
        """
        Check if the Sudoku board is a valid solution.

        Args:
            board (list of list of int): 2D list representing the Sudoku board.

        Returns:
            bool: True if the board is a valid solution, False otherwise.
        """
        raise NotImplementedError("This method must be overridden by subclasses")
