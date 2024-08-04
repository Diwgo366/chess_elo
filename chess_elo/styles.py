import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

VERDE = "#81B64C"
ROJO = "#FA412D"
AMARILLO = "#F7C631"

class FrameTematico(ttk.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.style = Style(theme='darkly')
        self.configure_styles()
        
    def configure_styles(self):
        self.style.configure("TLabel",
                             font = ('Ms Trebuchet', 12, 'bold'),
                             anchor="center"
                             )
        
        self.style.configure("Titulo.TLabel",
                             font = ('Ms Trebuchet', 20, 'bold'),
                             anchor="center"
                             )
        
        self.style.configure("Titulo.danger.TLabel",
                             font = ('Ms Trebuchet', 20, 'bold'),
                             anchor="center"
                             )
        
        self.style.configure("SubTitulo.TLabel",
                             font = ('Ms Trebuchet', 16, 'bold'),
                             anchor="center"
                             )
        
        self.style.configure("SubSubTitulo.TLabel",
                             font = ('Ms Trebuchet', 12, 'bold'),
                             anchor="center"
                             )
        
        self.style.configure("victoria.secondary.TCombobox",
                             bordercolor=VERDE,
                             )
        
        self.style.configure("derrota.secondary.TCombobox",
                             bordercolor=ROJO,
                             )
        
        self.style.configure("empate.secondary.TCombobox",
                             bordercolor=AMARILLO,
                             )
        
        self.style.configure("TButton",
                             font = ('Ms Trebuchet', 10, 'bold'),
                             )
        
        self.style.configure("secondary.TButton",
                             font = ('Ms Trebuchet', 16, 'bold'),
                             )
        
        self.style.configure("secondary.Treeview",
                             rowheight=25
                             )