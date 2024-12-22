import tkinter as tk
import customtkinter as ctk

# Function to add a new task
def add_task():
    task = task_entry.get()  # Get task from entry widget
    if task:  # Check if the task is not empty
        task_checkbox = ctk.CTkCheckBox(
            task_frame, 
            text=task,
            width=10,  # Adjust width of the checkbox
            height=10  # Adjust height of the checkbox
        )
        task_checkbox.pack(anchor="w", pady=5)  # Add checkbox to frame
        task_checkbox.configure(command=lambda cb=task_checkbox: remove_task(cb))  # Set command to remove task on click
        task_entry.delete(0, tk.END)  # Clear the entry field

# Function to remove task with fade animation (simulated by color change)
def remove_task(checkbox):
    def fade_out(widget, steps=10, step_size=10):
        if steps > 0:
            # Change the checkbox's color towards black (or the background color)
            new_color = f"#{step_size*steps:02x}{step_size*steps:02x}{step_size*steps:02x}"  # Darker color
            widget.configure(fg_color=new_color)
            widget.after(100, fade_out, widget, steps-1, step_size)  # Repeat with one fewer step
        else:
            widget.destroy()  # Remove widget after fade effect

    # Trigger the fade-out effect
    fade_out(checkbox)

# Initialize main window
root = ctk.CTk()

root.geometry("185x375+0+0")  # Position window at the top-left corner (x=0, y=0)

# Configure dark theme for customtkinter
ctk.set_appearance_mode("dark")  # Set dark mode for the app
ctk.set_default_color_theme("blue")  # Set default color theme to blue

# Create a frame to hold the task checkboxes
task_frame = ctk.CTkFrame(root, fg_color="black")
task_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Create a text entry field for tasks with smaller width
task_entry = ctk.CTkEntry(root, width=150, placeholder_text="Enter task...")
task_entry.pack(pady=10)

# Add task button
add_button = ctk.CTkButton(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
