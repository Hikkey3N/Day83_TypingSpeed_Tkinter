import tkinter as tk
from text_handling import TextBase
from time_app import TimerApp
import time

############################## GLOBAL VARIABLES ##############################
BG_COLOR = "#EA738D"

text_base = TextBase()
speed = 0.0

# Create the main window
root = tk.Tk()
timer = TimerApp(root)
root.configure(bg=BG_COLOR)


############################## Set Up User Interface ##############################
# Create a Label widget with customized appearance
label = tk.Label(root, 
                 text=text_base.generate_word(), 
                 font=("Helvetica", 16, "bold"),  # Set font style, size, and weight
                 bg=BG_COLOR,                      # Set background color to yellow
                 justify="center"                 # Center-align the text
                )
label.grid(row=1, column=1)

# Create a Text widget for user input
input_text = tk.Text(root, height=1, width=20, wrap=tk.NONE)
input_text.grid(row=2, column=1)

def check_count():
    current_text = input_text.get("1.0", tk.END)
    label_text = label.cget("text")
    print(label_text)
    print(current_text)

    if current_text == label_text:
        timer.get_elapsed_time()
        input_text.delete("1.0", tk.END)
    

# Binding the Return key to invoke the return timer
root.bind("<Return>", lambda event: check_count())


# Start the timer
timer.start_timer()

# Start the Tkinter event loop
root.mainloop()
