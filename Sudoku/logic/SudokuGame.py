from logic.Board import Board  # Import the Board class
from logic.Solver import Solver  # Import the Solver class
from interface.SudokuGameInterface import SudokuGameInterface  # Import the SudokuGameInterface class


class SudokuGame(SudokuGameInterface):  # Define the SudokuGame class inheriting from SudokuGameInterface
    def __init__(self):
        """
        Initialize the Sudoku game.
        """
        try:
            self.board = Board()  # Create an instance of the Board class
            self.solver = Solver()  # Create an instance of the Solver class
            self.difficulty = 36  # Set the default difficulty level
        except Exception as e:
            print(f"Error initializing the game: {e}")

    def start_game(self):
        """
        Starts a new game by resetting the board, solving it, and then removing some numbers based on difficulty.
        """
        try:
            self.board.reset_board()  # Reset the board to an empty state
            self.board.fill_grid()  # Fill the board with a valid solution
            self.board.remove_numbers(self.difficulty)  # Remove numbers to create the puzzle
        except Exception as e:
            print(f"Error starting the game: {e}")

    def check_move(self, row, col, value):
        """
        Checks if a move is valid before placing a number on the board.
        :param row: The row index of the cell
        :param col: The column index of the cell
        :param value: The value to be placed in the cell
        :return: True if the move is valid, False otherwise
        """
        try:
            if self.board.grid[row][col].is_fixed():  # Check if the cell is fixed (pre-filled and cannot be changed)
                return False  # Return False if the cell is fixed
            if not self.solver.is_valid(self.board.get_values(), value, (row, col)):  # Check if the move is valid according to Sudoku rules
                return False  # Return False if the move is not valid
            self.board.grid[row][col].value = value  # Place the number on the board if valid
            return True  # Return True if the move is valid
        except Exception as e:
            print(f"Error checking move at ({row}, {col}) with value {value}: {e}")
            return False

    def solve_game(self):
        """
        Solves the current state of the Sudoku board.
        """
        try:
            temp_board = self.board.get_values()  # Get the current board values
            self.solver.solve(temp_board)  # Solve the board
            self.board.set_values(temp_board)  # Set the board with the solved values
        except Exception as e:
            print(f"Error solving the game: {e}")

    def set_difficulty(self, difficulty):
        """
        Sets the game difficulty.
        :param difficulty: The difficulty level to set
        """
        try:
            self.difficulty = difficulty  # Assign the difficulty value
        except Exception as e:
            print(f"Error setting difficulty: {e}")

    def generate_puzzle(self):
        """
        Generates a new puzzle.
        """
        try:
            self.board.fill_grid()  # Fill the board with a valid solution
            self.board.remove_numbers(self.difficulty)  # Remove numbers to create the puzzle based on difficulty
        except Exception as e:
            print(f"Error generating puzzle: {e}")

    def is_solution_correct(self):
        """
        Checks if the entire board is correctly solved.
        :return: True if the board is solved correctly, False otherwise
        """
        try:
            # Check each row for duplicates
            for row in self.board.grid:  # Iterate through each row
                if len(set(cell.value for cell in row if cell.value != 0)) != 9:  # Check if the row has all unique numbers from 1-9
                    return False  # Return False if there are duplicates

            # Check each column for duplicates
            for col in range(9):  # Iterate through each column index
                col_values = [self.board.grid[row][col].value for row in range(9) if self.board.grid[row][col].value != 0]  # Collect values in the column
                if len(set(col_values)) != 9:  # Check if the column has all unique numbers from 1-9
                    return False  # Return False if there are duplicates

            # Check each 3x3 square for duplicates
            for start_row in range(0, 9, 3):  # Iterate through each 3x3 square starting row index
                for start_col in range(0, 9, 3):  # Iterate through each 3x3 square starting column index
                    block_values = []  # Initialize an empty list for block values
                    for row in range(start_row, start_row + 3):  # Iterate through each row in the 3x3 square
                        for col in range(start_col, start_col + 3):  # Iterate through each column in the 3x3 square
                            cell_value = self.board.grid[row][col].value  # Get the cell value
                            if cell_value != 0:  # If the cell is not empty
                                block_values.append(cell_value)  # Add the value to the block values list
                    if len(set(block_values)) != 9:  # Check if the 3x3 square has all unique numbers from 1-9
                        return False  # Return False if there are duplicates

            return True  # Return True if no duplicates are found in rows, columns, and 3x3 squares
        except Exception as e:
            print(f"Error checking if the solution is correct: {e}")
            return False
