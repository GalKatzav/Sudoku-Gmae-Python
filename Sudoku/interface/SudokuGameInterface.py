class SudokuGameInterface:

    def start_game(self):
        """
        Start a new game by resetting the board, solving it, and then removing some numbers based on difficulty.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def check_move(self, row, col, value):
        """
        Check if a move is valid before placing a number on the board.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to place in the cell.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def solve_game(self):
        """
        Solve the current state of the Sudoku board.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def set_difficulty(self, difficulty):
        """
        Set the game difficulty.

        Args:
            difficulty (str): The difficulty level to set (e.g., 'easy', 'medium', 'hard').
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def generate_puzzle(self):
        """
        Generate a new puzzle by solving the board and then removing numbers according to the current difficulty.
        """
        raise NotImplementedError("This method must be overridden by subclasses")

    def is_solution_correct(self):
        """
        Check if the entire board is correctly solved.

        Returns:
            bool: True if the solution is correct, False otherwise.
        """
        raise NotImplementedError("This method must be overridden by subclasses")
