import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

class GraphView:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(fill="both", expand=True)

        self.label = tk.Label(frame, text="Privilege Graph")
        self.label.pack()

        self.canvas = tk.Label(frame)
        self.canvas.pack()

        self.refresh_button = tk.Button(frame, text="Refresh Graph", command=self.load_graph)
        self.refresh_button.pack()

        self.open_browser_button = tk.Button(frame, text="Open Interactive Graph", command=self.open_in_browser)
        self.open_browser_button.pack()

    def load_graph(self):
        try:
            img = Image.open("graph.png")
            img = img.resize((800, 600))
            self.imgtk = ImageTk.PhotoImage(img)
            self.canvas.config(image=self.imgtk)
        except Exception as e:
            self.canvas.config(text=f"Error loading graph: {e}")

    def open_in_browser(self):
        webbrowser.open("graph.html")
