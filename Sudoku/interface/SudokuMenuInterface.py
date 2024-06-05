class SudokuMenuInterface:

    def initialize_game(self):
        """
        Initialize the game by creating the game window and starting the game.
        """
        raise NotImplementedError

    def start_game(self):
        """
        Start a new game by resetting the board, filling it with numbers, and clearing cells based on the difficulty level.
        """
        raise NotImplementedError

    def cell_click(self, pos):
        """
        Handle cell click events on the game canvas. Select the clicked cell and deselect any previously selected cell.

        Args:
            pos (tuple): The position of the click event (x, y coordinates).
        """
        raise NotImplementedError

    def key_input(self, key):
        """
        Handle key input events on the game canvas. Set the value of the selected cell based on the key input.

        Args:
            key (int): The key code of the input.
        """
        raise NotImplementedError

    def update_screen(self):
        """
        Update the game canvas or display area to reflect the current state of the Sudoku board.
        """
        raise NotImplementedError

    def draw_grid(self):
        """
        Draw the Sudoku grid on the screen.
        """
        raise NotImplementedError

    def is_board_full(self):
        """
        Check if the Sudoku board is fully filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        raise NotImplementedError

    def check_solution(self):
        """
        Check if the current solution on the board is valid. Display a message or take appropriate action
        based on whether the solution is correct or not.
        """
        raise NotImplementedError

    def ask_replay(self):
        """
        Ask the user if they want to play again after completing a game. Restart the game if the user chooses to play again.
        """
        raise NotImplementedError
