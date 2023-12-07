import tkinter as tk
tk.Tk.mainloop()

def on_button_click():
    label.config(text="Hello, GUI App!")


# Create the main window
app = tk.Tk()
app.title("My GUI App")

#Create a button
butto = tk.Button(app, text="Click me!", command=on_button_click)
butto.pack(pady=10)

# Create a label
label = tk.Label(app, text="Welcome to my GUI App!")
label.pack(pady=10 )

# Start the main event loop
app.mainloop

