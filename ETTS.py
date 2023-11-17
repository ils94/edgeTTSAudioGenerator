import tkinter as tk
from tkinter import ttk, filedialog
import edgeTTSEngine
import asyncio
import voices
import os


def center_window(window, min_width, min_height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates for centering
    x = (screen_width - min_width) // 2
    y = (screen_height - min_height) // 2

    # Set the window's geometry to center it on the screen
    window.geometry(f"{min_width}x{min_height}+{x}+{y}")


def generate_audio():
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if output_file:  # If a file name is provided
        asyncio.run(edgeTTSEngine.engine(text_widget.get("1.0", "end").strip(), combo_box.get(), output_file))


def on_resize(event):
    text_widget.config(height=root.winfo_height() // 30)


def load_list():
    # Replace this example list with your own list of elements
    elements = voices.voice_list
    for element in elements:
        combo_box['values'] = (*combo_box['values'], element)


root = tk.Tk()
root.title("Edge-TTS Audio Generator")
root.geometry("500x500")
root.minsize(500, 500)
if os.path.isfile("icon.ico"):
    root.iconbitmap("icon.ico")

root.bind("<Configure>", on_resize)

frame_1 = ttk.Frame(root)
frame_1.pack(fill="x")

combo_box = ttk.Combobox(frame_1, state="readonly")
combo_box.pack(side="left", padx=10, pady=5)

# Load the list of elements into the ComboBox
load_list()

# Set a default value for the ComboBox
if combo_box['values']:
    combo_box.current(104)  # Set the first element as default

text_widget = tk.Text(root)
text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Audio", command=generate_audio)
generate_button.pack(anchor=tk.NW, padx=10, pady=5)

center_window(root, 500, 500)

root.mainloop()
