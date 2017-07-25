import tkinter as tk

class Budget_View():
    def __init__(self):
        self._root_window = tk.Tk()

        self._selection_option = tk.Canvas(
            master = self._root_window, width = 600, height = 200,
            background = 'white')
        
        self._selection_option.grid(row = 0, column = 0, padx = 10, pady = 10,
            sticky = tk.N + tk.S + tk.E + tk.W)
    
Budget_View()
