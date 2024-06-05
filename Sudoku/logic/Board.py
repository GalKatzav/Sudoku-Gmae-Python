import random  # Import the random module
from logic.Solver import Solver  # Import the Solver class
from logic.Cell import Cell  # Import the Cell class
from interface.BoardInterface import BoardInterface  # Import the BoardInterface class


class Board(BoardInterface):  # Define the Board class inheriting from BoardInterface
    def __init__(self):
        """
        Initialize the board with a 9x9 grid of cells.
        """
        try:
            self.grid = [[Cell(row, col, 550 // 9) for col in range(9)] for row in range(9)]  # Create a 9x9 grid of Cell objects
        except Exception as e:
            print(f"Error initializing the board: {e}")

    def reset_board(self):
        """
        Reset the board to an empty state with a 9x9 grid of cells.
        """
        try:
            self.grid = [[Cell(row, col, 550 // 9) for col in range(9)] for row in range(9)]  # Reset the grid with new Cell objects
        except Exception as e:
            print(f"Error resetting the board: {e}")

    def fill_grid(self):
        """
        Fill the grid with a valid Sudoku solution using the Solver.
        """
        try:
            solver = Solver()  # Create an instance of the Solver
            temp_board = [[0 for _ in range(9)] for _ in range(9)]  # Create a temporary 9x9 grid filled with zeros
            self.shuffle_board(temp_board)  # Shuffle the board to introduce variability
            solver.solve(temp_board)  # Solve the temporary board to generate a Sudoku solution
            if solver.has_unique_solution(temp_board):  # Ensure the puzzle has a unique solution
                for row in range(9):  # Iterate through each row
                    for col in range(9):  # Iterate through each column
                        self.grid[row][col] = Cell(row, col, 550 // 9, value=temp_board[row][col],
                                                   fixed=True)  # Fill the grid with solved values
            else:
                self.fill_grid()  # Retry if the generated puzzle does not have a unique solution
        except Exception as e:
            print(f"Error filling the grid: {e}")

    def shuffle_board(self, board):
        """
        Shuffle the board to introduce variability.
        :param board: 2D list representing the Sudoku board
        """
        numbers = list(range(1, 10))  # Create a list of numbers 1-9
        random.shuffle(numbers)  # Shuffle the numbers list
        for i in range(9):  # Iterate through the board
            board[i][i] = numbers[i]  # Assign shuffled numbers diagonally

    def remove_numbers(self, difficulty):
        """
        Remove numbers from the filled grid to create a Sudoku puzzle of the given difficulty.
        :param difficulty: Number of cells to be removed to create the puzzle
        """
        try:
            num_remove = difficulty  # Set the number of cells to remove based on difficulty
            count = 0  # Initialize a counter for removed cells
            while count < num_remove:  # Continue until the required number of cells are removed
                row = random.randint(0, 8)  # Generate a random row index
                col = random.randint(0, 8)  # Generate a random column index
                if self.grid[row][col].value != 0:  # Check if the cell is not already empty
                    self.grid[row][col].value = 0  # Set the cell value to 0 (empty)
                    self.grid[row][col].fixed = False  # Mark the cell as not fixed
                    count += 1  # Increment the counter
        except Exception as e:
            print(f"Error removing numbers: {e}")

    def get_values(self):
        """
        Get the current values of the board.
        :return: 2D list representing the current values of the board
        """
        try:
            return [[cell.value for cell in row] for row in self.grid]  # Return a 2D list of cell values
        except Exception as e:
            print(f"Error getting board values: {e}")
            return []

    def set_values(self, values):
        """
        Set the values of the board to the given values.
        :param values: 2D list representing the values to set on the board
        """
        try:
            for row in range(9):  # Iterate through each row
                for col in range(9):  # Iterate through each column
                    self.grid[row][col].value = values[row][col]  # Set the cell value to the given value
        except Exception as e:
            print(f"Error setting board values: {e}")
