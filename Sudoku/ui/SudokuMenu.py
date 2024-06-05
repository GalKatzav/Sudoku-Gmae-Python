import pygame  # Import the Pygame library
import random  # Import the random module

from logic.Board import Board  # Import the Board class
from logic.Solver import Solver  # Import the Solver class
from logic.Cell import Cell  # Import the Cell class
from ui.Button import Button  # Import the Button class
from ui.InputBox import InputBox  # Import the InputBox class

pygame.init()  # Initialize Pygame

# Define constants for the game
WINDOW_SIZE = 550  # The new size of the game window
CELL_SIZE = WINDOW_SIZE // 9  # The size of each cell
FPS = 30  # Frames per second
FOOTER_HEIGHT = 50  # Height of the footer where the buttons are located

# Colors
WHITE = (255, 255, 255)  # RGB color for white
BLACK = (0, 0, 0)  # RGB color for black
GRAY = (200, 200, 200)  # RGB color for gray
BLUE = (0, 0, 255)  # RGB color for blue
RED = (255, 0, 0)  # RGB color for red

# Font
font = pygame.font.SysFont('Arial', 24)  # Set the font for drawing text


class SudokuMenu:
    def __init__(self):
        """
        Initialize the Sudoku game menu.
        """
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + FOOTER_HEIGHT))  # Create the game window
        pygame.display.set_caption("Sudoku Game")  # Set the window title
        self.board = Board()  # Create a Board instance
        self.solver = Solver()  # Create a Solver instance
        self.cells = [[Cell(row, col, CELL_SIZE) for col in range(9)] for row in range(9)]  # Create a 9x9 grid of Cell instances
        self.selected_cell = None  # Initialize the selected cell as None
        self.buttons = []  # List to store buttons

        self.create_menu()  # Create the menu
        self.difficulty = self.get_difficulty()  # Get the difficulty from the user
        self.start_game()  # Start a new game

    def create_menu(self):
        """
        Create the menu for the Sudoku game.
        """
        font = pygame.font.SysFont('Arial', 24)  # Set the font for the buttons
        button_y = WINDOW_SIZE + 10  # Set the y-coordinate for the buttons
        self.buttons.append(Button("New Game", (50, button_y), font))  # Create the "New Game" button
        self.buttons.append(Button("Check Me", (200, button_y), font))  # Create the "Check Me" button
        self.buttons.append(Button("Quit", (350, button_y), font))  # Create the "Quit" button

    def draw_menu(self):
        """
        Draw the menu on the screen.
        """
        for button in self.buttons:  # Iterate through the buttons
            button.show(self.screen)  # Show each button on the screen

    def handle_menu(self, event):
        """
        Handle menu interactions.
        """
        for button in self.buttons:  # Iterate through the buttons
            if button.click(event):  # Check if a button is clicked
                if button.feedback == "New Game":
                    self.difficulty = self.get_difficulty()  # Get the difficulty from the user
                    self.start_game()  # Start a new game
                elif button.feedback == "Check Me":
                    self.check_solution()  # Check the current solution
                elif button.feedback == "Quit":
                    pygame.quit()  # Quit Pygame
                    exit()  # Exit the program

    def start_game(self):
        """
        Start a new game by resetting the board, solving it, and then removing some numbers based on difficulty.
        """
        self.board.reset_board()  # Reset the board
        self.board.fill_grid()  # Fill the board with a solved Sudoku grid
        if self.difficulty == 'easy':
            num_clear = random.randint(50, 67)  # Define the number of cells to clear for easy difficulty
        elif self.difficulty == 'medium':
            num_clear = random.randint(32, 49)  # Define the number of cells to clear for medium difficulty
        elif self.difficulty == 'hard':
            num_clear = random.randint(28, 31)  # Define the number of cells to clear for hard difficulty
        else:
            num_clear = 36  # Default number if difficulty is not set properly
        self.board.remove_numbers(81 - num_clear)  # Remove numbers from the board to create the puzzle
        self.update_cells()  # Update cells with the current board state
        self.update_screen()  # Update the screen with the current board state

    def update_cells(self):
        """
        Update the cell values from the board.
        """
        for row in range(9):  # Iterate through each row
            for col in range(9):  # Iterate through each column
                self.cells[row][col].set_value(self.board.grid[row][col].value)  # Set the value for each cell

    def cell_click(self, pos):
        """
        Handle cell click events to select a cell.
        :param pos: The position of the mouse click
        """
        col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE  # Calculate the column and row index based on click position
        if 0 <= col < 9 and 0 <= row < 9:  # Check if the click is within the board boundaries
            if self.selected_cell:  # If a cell is already selected
                self.selected_cell.deselect()  # Deselect the currently selected cell
            self.selected_cell = self.cells[row][col]  # Update the selected cell
            self.selected_cell.select()  # Select the new cell

    def key_input(self, key):
        """
        Handle key input events to set cell values.
        :param key: The key that was pressed
        """
        if self.selected_cell and key in range(pygame.K_1, pygame.K_9 + 1):  # Check if a valid digit key is pressed
            self.selected_cell.set_value(key - pygame.K_0, BLACK)  # Set the value of the selected cell
            self.board.grid[self.selected_cell.row][self.selected_cell.col].value = key - pygame.K_0  # Update the board with the new value
            self.check_after_move()  # Check the solution after each move

    def check_after_move(self):
        """
        Check the solution after each move.
        """
        if self.is_board_full():  # Check if the board is full
            if self.solver.is_valid_solution(self.board.get_values()):  # Validate the solution using the Solver
                print("Congratulations! You solved the puzzle!")  # Print success message
                self.ask_replay()  # Ask the player if they want to play again

    def update_screen(self):
        """
        Update the screen with the current values of the board.
        """
        self.screen.fill(WHITE)  # Fill the screen with white color
        self.draw_grid()  # Draw the Sudoku grid
        for row in range(9):  # Iterate through each row
            for col in range(9):  # Iterate through each column
                self.cells[row][col].draw(self.screen, font)  # Draw each cell
        self.draw_menu()  # Draw the menu
        pygame.display.flip()  # Update the display

    def draw_grid(self):
        """
        Draw the Sudoku grid on the screen.
        """
        for x in range(0, WINDOW_SIZE, CELL_SIZE):  # Draw vertical lines
            pygame.draw.line(self.screen, BLACK if x % (3 * CELL_SIZE) == 0 else GRAY, (x, 0), (x, WINDOW_SIZE))
        for y in range(0, WINDOW_SIZE, CELL_SIZE):  # Draw horizontal lines
            pygame.draw.line(self.screen, BLACK if y % (3 * CELL_SIZE) == 0 else GRAY, (0, y), (WINDOW_SIZE, y))

    def is_board_full(self):
        """
        Check if the board is completely filled.
        :return: True if the board is full, False otherwise
        """
        return all(self.board.grid[row][col].value != 0 for row in range(9) for col in range(9))  # Check if all cells are filled

    def check_solution(self):
        """
        Check if the current board is a valid Sudoku solution.
        """
        correct = True
        for row in range(9):  # Iterate through each row
            for col in range(9):  # Iterate through each column
                if not self.solver.is_valid(self.board.get_values(), self.board.grid[row][col].value, (row, col)):  # Validate each cell
                    self.cells[row][col].set_color(RED)  # Highlight errors in red
                    correct = False  # Mark as incorrect
                elif not self.cells[row][col].fixed:  # Only reset color for non-fixed cells
                    self.cells[row][col].set_color(BLACK)  # Reset to black if correct
        if correct:
            print("Congratulations! You solved the puzzle!")  # Print success message
            self.ask_replay()  # Ask the player if they want to play again
        else:
            print("There are errors in the puzzle!")  # Print error message

    def ask_replay(self):
        """
        Ask the player if they want to play again.
        """
        input_box = InputBox(150, 300, 200, 40, font)  # Create an input box with font
        done = False
        while not done:  # Loop until done
            for event in pygame.event.get():  # Iterate through events
                if event.type == pygame.QUIT:  # Quit event
                    pygame.quit()  # Quit Pygame
                    exit()  # Exit program
                result = input_box.handle_event(event)  # Handle input box events
                if result:  # If result is returned
                    response = result.lower()  # Convert to lowercase
                    done = True  # Exit loop

            self.screen.fill(WHITE)  # Fill screen with white
            input_box.draw(self.screen)  # Draw input box
            prompt_surface = font.render("Congratulations!"
                                         "Do you want to play again? (yes/no): ", True, BLACK)  # Render prompt
            self.screen.blit(prompt_surface, (50, 250))  # Draw prompt
            pygame.display.flip()  # Update display

        if response == 'yes':  # If the player wants to play again
            difficulty = self.get_difficulty()  # Get the difficulty
            self.difficulty = difficulty  # Set the difficulty
            self.start_game()  # Start a new game
        else:
            pygame.quit()  # Quit Pygame
            exit()  # Exit the program

    def get_difficulty(self):
        """
        Prompt the player to enter the difficulty level.
        :return: The chosen difficulty level
        """
        input_box = InputBox(150, 300, 200, 40, font)  # Create an input box with font
        done = False
        while not done:  # Loop until done
            for event in pygame.event.get():  # Iterate through events
                if event.type == pygame.QUIT:  # Quit event
                    pygame.quit()  # Quit Pygame
                    exit()  # Exit program
                result = input_box.handle_event(event)  # Handle input box events
                if result:  # If result is returned
                    response = result.lower()  # Convert to lowercase
                    if response in ['easy', 'medium', 'hard']:  # Check if valid difficulty
                        done = True  # Exit loop

            self.screen.fill(WHITE)  # Fill screen with white
            input_box.draw(self.screen)  # Draw input box
            prompt_surface = font.render("Enter difficulty (easy, medium, hard): ", True, BLACK)  # Render prompt
            self.screen.blit(prompt_surface, (50, 250))  # Draw prompt
            pygame.display.flip()  # Update display

        return response  # Return the chosen difficulty

    @staticmethod
    def main():
        """
        The main function to run the game.
        """
        app = SudokuMenu()  # Create the SudokuMenu application

        clock = pygame.time.Clock()  # Create a clock object to control the frame rate
        running = True  # Set the running flag to True

        while running:  # Main game loop
            for event in pygame.event.get():  # Iterate through the event queue
                if event.type == pygame.QUIT:  # If the quit event is triggered
                    running = False  # Set the running flag to False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # If a mouse button is pressed
                    app.cell_click(pygame.mouse.get_pos())  # Handle the cell click event
                    app.handle_menu(event)  # Handle the menu click event
                elif event.type == pygame.KEYDOWN:  # If a key is pressed
                    app.key_input(event.key)  # Handle key input events

            app.update_screen()  # Update the screen
            clock.tick(FPS)  # Control the frame rate

        pygame.quit()  # Quit Pygame


