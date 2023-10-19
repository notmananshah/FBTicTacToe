import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Create the main Tkinter window
window = tk.Tk()
window.title("Football Tic-Tac-Toe")

# Create a 4x4 grid of buttons and labels
buttons = []
row_labels = []
column_labels = []
for i in range(4):
    row = []
    for j in range(4):
        if i == 0 and j == 0:
            # Create a blank label for the top-left corner
            label = tk.Label(window, text="", font=("Arial", 12, "bold"))
            label.grid(row=i, column=j)
        elif i == 0:
            # Prompt user input for column labels
            column_name = simpledialog.askstring("Column Label", f"Enter label for Column {j}")
            label = tk.Label(window, text=column_name, font=("Arial", 12, "bold"))
            label.grid(row=i, column=j)
            column_labels.append(label)
        elif j == 0:
            # Prompt user input for row labels
            row_name = simpledialog.askstring("Row Label", f"Enter label for Row {i}")
            label = tk.Label(window, text=row_name, font=("Arial", 12, "bold"))
            label.grid(row=i, column=j)
            row_labels.append(label)
        else:
            # Create buttons for the game grid
            button = tk.Button(window, text="", width=10, height=5, font=("Arial", 24))
            button.grid(row=i, column=j)
            row.append(button)
    if row:  # Check if the row actually contains buttons
        buttons.append(row)

# Function to handle button clicks
def button_click(row, col):
    global turn  # Declare turn as global before using it
    if buttons[row][col]["text"] == "":
        player = "Player 1" if turn % 2 == 0 else "Player 2"
        symbol = simpledialog.askstring("Symbol Entry", f"Enter symbol for {player}")
        color = "blue" if turn % 2 == 0 else "red"
        buttons[row][col]["text"] = symbol
        buttons[row][col]["fg"] = color

        # Check for a win condition
        if check_win(color):  # Adjusted to pass color instead of symbol
            messagebox.showinfo("Game Over", f"{player} wins!")
            window.quit()
        elif turn == 8:
            messagebox.showinfo("Game Over", "It's a draw!")
            window.quit()

        turn += 1


# Function to check for a win condition
def check_win(color):
    for i in range(3):
        if (
            buttons[i][0]["fg"] == buttons[i][1]["fg"] == buttons[i][2]["fg"] == color
            or buttons[0][i]["fg"] == buttons[1][i]["fg"] == buttons[2][i]["fg"] == color
            or buttons[0][0]["fg"] == buttons[1][1]["fg"] == buttons[2][2]["fg"] == color
            or buttons[2][0]["fg"] == buttons[1][1]["fg"] == buttons[0][2]["fg"] == color
        ):
            return True
    return False


turn = 0

# A function to create a button command
def create_button_command(row, col):
    return lambda: button_click(row, col)

# Start the game
for i in range(3):
    for j in range(3):
        buttons[i][j]["command"] = create_button_command(i, j)

# Run the Tkinter event loop
window.mainloop()
