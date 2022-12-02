import tkinter as tk

root = tk.Tk()

greeting = tk.Label(root, text="Hello, Tkinter")
greeting.pack()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()

entry = tk.Entry()
entry.pack()
entry.insert(0, "Real ")

text_box = tk.Text()
text_box.pack()

root.mainloop()