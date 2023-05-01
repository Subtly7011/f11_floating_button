import tkinter as tk
import os

def on_button_press(event=None):
    os.system(r'script.ahk')

root = tk.Tk()
root.overrideredirect(1) # hide window decorations
root.withdraw()          # hide root window

button_window = tk.Toplevel(root) # create a new window for the button
button_window.overrideredirect(1) # hide window decorations
button_window.geometry('50x25+100+100') # set button size and position
button_window.attributes('-topmost', True) # set as always on top

button = tk.Button(button_window, text="F11", command=on_button_press)
button.pack(fill='both', expand=1)
button.bind('<Button-3>', lambda e: root.destroy())
root.mainloop()
