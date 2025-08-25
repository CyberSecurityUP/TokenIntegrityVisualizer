import tkinter as tk
import json

class ChecklistView:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side="right", fill="both", expand=True)

        self.label = tk.Label(frame, text="Hardening Checklist")
        self.label.pack()

        with open("data/hardening_checklist.json") as f:
            checklist = json.load(f)

        for item in checklist:
            tk.Checkbutton(frame, text=item).pack(anchor="w")
