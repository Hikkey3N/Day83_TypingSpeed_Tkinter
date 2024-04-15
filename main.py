import tkinter as tk
from tkinter import messagebox
from text_handling import TextBase

############################## GLOBAL VARIABLES ##############################
BG_COLOR = "#EA738D"

##########################################################################################

text_base = TextBase()

# Create the main window
root = tk.Tk()
root.configure(bg=BG_COLOR)

############################## Timer ##############################
def update_timer():
    global elapsed_time
    # Update the label with the elapsed time
    timer_label.config(text=f"Elapsed Time: {elapsed_time} seconds")
    elapsed_time += 1
    # Schedule the update_timer function to be called again after 1000 milliseconds (1 second)
    root.after(1000, update_timer)

def reset_timer():
    global elapsed_time
    elapsed_time = 0
    update_timer()

# Initialize the elapsed time
elapsed_time = 0

# Create a label to display the timer
timer_label = tk.Label(root, text="Elapsed Time: 0 seconds")
timer_label.grid(row=0, column=1)

############################## Set Up User Interface ##############################
def submit_text():
    # Retrieve the text from the input_text widget
    user_input = input_text.get("1.0", tk.END)
    # Print or process the user input
    print("User input:", user_input)

# Create a Label widget with customized appearance
label = tk.Label(root, 
                 text=text_base.generate_sentence(), 
                 font=("Helvetica", 16, "bold"),  # Set font style, size, and weight
                 bg=BG_COLOR,                      # Set background color to yellow
                 justify="center"                 # Center-align the text
                )
label.grid(row=1, column=1)

# Create a Text widget for user input
input_text = tk.Text(root, height=2, width=20)
input_text.grid(row=2, column=1)

# Create a button to submit the text
submit_button = tk.Button(root, text="Submit", command=reset_timer)
submit_button.grid(row=3, column=1)


# Start the timer
update_timer()











# Start the Tkinter event loop
root.mainloop()

