import tkinter as tk


class Selection_Menu():
    def __init__(self, master):
        self.canvas = tk.Canvas(
            master = master, width = 600, height = 200,
            background = 'white')

        wefewf


    def _select_add(self):
        pass
    


class Budget_View():
    def __init__(self):
        self._root_window = tk.Tk()
        self._selection = Selection_Menu(self._root_window)
        
        
        self._selection.canvas.grid(row = 0, column = 0, padx = 10, pady = 10,
            sticky = tk.N + tk.S + tk.E + tk.W)


    
Budget_View()


