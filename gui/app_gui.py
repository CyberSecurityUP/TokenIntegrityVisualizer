import tkinter as tk
from tkinter import ttk
from gui.process_list_view import ProcessListView
from gui.graph_view import GraphView
from gui.checklist_view import ChecklistView

class TokenIntegrityApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Token & Integrity Visualizer - by Joas A Santos")
        self.root.geometry("1000x700")

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        # Tabs
        process_frame = tk.Frame(notebook)
        ProcessListView(process_frame)
        notebook.add(process_frame, text="Processes & Tokens")

        graph_frame = tk.Frame(notebook)
        GraphView(graph_frame)
        notebook.add(graph_frame, text="Privilege Graph")

        checklist_frame = tk.Frame(notebook)
        ChecklistView(checklist_frame)
        notebook.add(checklist_frame, text="Hardening Checklist")

    def run(self):
        self.root.mainloop()
