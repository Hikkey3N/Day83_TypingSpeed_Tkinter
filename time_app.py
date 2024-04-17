import tkinter as tk

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.bg_color = "#EA738D"
        self.elapsed_time = 0
        self.timer_running = False
        self.timer_event = None
        self.total_time = 0

        # Initialize the timer label
        self.timer_label = tk.Label(self.master, text="Elapsed Time: 0 seconds")
        self.timer_label.grid(row=0, column=1, padx=10, pady=10)


    def start_timer(self):
        # Start the timer if not already running
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        # Update the timer label with the elapsed time if the timer is running
        if self.timer_running:
            self.timer_label.config(text=f"Elapsed Time: {self.elapsed_time} seconds")
            self.elapsed_time += 1
            # Schedule the update_timer function to be called again after 1000 milliseconds (1 second)
            self.timer_event = self.master.after(1000, self.update_timer)

    def reset_timer(self):
        # Stop the timer and reset the elapsed time
        self.timer_running = False
        self.elapsed_time = 0
        self.timer_label.config(text="Elapsed Time: 0 seconds")
        # Cancel any pending timer events
        if self.timer_event:
            self.master.after_cancel(self.timer_event)
            
        self.start_timer()

    def get_elapsed_time(self):
        temp_time = self.elapsed_time
        self.total_time += (temp_time - 1)
        self.reset_timer()
        print(self.total_time)
        

