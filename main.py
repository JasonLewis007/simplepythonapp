import tkinter as tk


def on_button_click():
    """Function triggered when the button is clicked."""
    label.config(text="Button clicked! Welcome to my GUI App!")


# Initialize the main window
app = tk.Tk()
app.title("My Amazing GUI App")

# Create a button with a descriptive command text and bind it to the function
button = tk.Button(
    app,
    text="Click me to see magic!",
    command=on_button_click,
    # Add padding for better visual appeal
    padx=10,
    pady=10,
)

# Pack the button in the window
button.pack()

# Create and configure the label with initial text
label = tk.Label(app, text="Click the button to get started!", font=("Arial", 12))

# Pack the label with padding
label.pack(pady=10)

# Start the main event loop
app.mainloop()



