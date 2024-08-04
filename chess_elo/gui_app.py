import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from client.styles import FrameTematico
import datetime
from model.partidas_dao import Jugador, guardar_jugador, listar_jugadores, nombre_existente, obtener_jugador, actualizar_jugador, Partida, guardar_partida, listar_partidas

class Frame_inicio(FrameTematico):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.campo_bienvenida()
        
    def campo_bienvenida(self):
        
        #Labels:
        self.label_titulo = ttk.Label(self, text="Bienvenido al Bunker Elo", style="Titulo.TLabel")
        self.label_titulo.grid(row=0, column=0, columnspan=3, padx=40, pady=(20,10))
        
        #Botones
        def boton_registrar():
            nuevo_frame = Frame_tipo(self.root, tipo = "Registro")
            nuevo_frame.pack()
            self.forget()
            
        self.imagen_registro = Image.open("img/ch-registro.png")
        self.imagen_registro = self.imagen_registro.resize((40, 40))
        self.icono_registro = ImageTk.PhotoImage(self.imagen_registro)
        
        boton_registro = ttk.Button(self, text="  Registrar Partida", width=20, image=self.icono_registro, command=boton_registrar, compound=tk.LEFT, style="secondary.TButton")
        boton_registro.grid(row=1, column=0, columnspan=3, pady=5)
        
        def boton_ranking():
            nuevo_frame = Frame_tipo(self.root, tipo = "Ranking")
            nuevo_frame.pack()
            self.forget()
            
        self.imagen_ranking = Image.open("img/ch-ranking.png")
        self.imagen_ranking = self.imagen_ranking.resize((40, 40))
        self.icono_ranking = ImageTk.PhotoImage(self.imagen_ranking)
        
        self.boton_ranking = ttk.Button(self, text="  Ver Ranking", width=20, image=self.icono_ranking, command=boton_ranking, compound=tk.LEFT, style="secondary.TButton")
        self.boton_ranking.grid(row=2, column=0, columnspan=3, pady=5)
        
        def boton_torneo():
            nuevo_frame = Frame_torneo(self.root)
            nuevo_frame.pack()
            self.forget()
        
        self.imagen_torneo = Image.open("img/ch-torneo.png")
        self.imagen_torneo = self.imagen_torneo.resize((40, 40))
        self.icono_torneo = ImageTk.PhotoImage(self.imagen_torneo)
        
        self.boton_torneo = ttk.Button(self, text="  Crear Torneo", width=20, image=self.icono_torneo, command=boton_torneo, compound=tk.LEFT, style="secondary.TButton")
        self.boton_torneo.grid(row=3, column=0, columnspan=3, pady=5)
        
        def boton_historial_general():
            nuevo_frame = Frame_historial(self.root, tipo = None)
            nuevo_frame.pack()
            self.forget()
            
        self.imagen_historial = Image.open("img/ch-historial.png")
        self.imagen_historial = self.imagen_historial.resize((40, 40))
        self.icono_historial = ImageTk.PhotoImage(self.imagen_historial)
        
        self.boton_historial = ttk.Button(self, text="  Ver Historial", width=20, image=self.icono_historial, command=boton_historial_general, compound=tk.LEFT, style="secondary.TButton")
        self.boton_historial.grid(row=4, column=0, columnspan=3, pady=5)
        
        #Boton de salir
        def boton_salir():
            self.root.destroy()
        
        self.button_salida = ttk.Button(self, text='Salir', command=boton_salir, style="danger.TButton", width=10)
        self.button_salida.grid(row=5, column=2, pady=(5,20))

class Frame_tipo(FrameTematico):
    def __init__(self, root = None, tipo = None):
        super().__init__(root)
        self.root = root
        self.tipo = tipo
        self.pack()
        self.campo_tipos()
        
    def campo_tipos(self):
        #Labels:
        if self.tipo == "Registro":
            texto = "Tipo de Partida a Registrar"
        elif self.tipo == "Ranking":
            texto = "Tipo de Partida a Rankear"

        self.label_titulo = ttk.Label(self, text=texto, style="Titulo.TLabel")
        self.label_titulo.grid(row=0, column=0, columnspan=3, padx=30, pady=(20,5))
        
        #Botones
        def blitz3():
            if self.tipo == "Registro":
                nuevo_frame = Frame_registro(self.root, tipo = "blitz3")
            elif self.tipo == "Ranking":
                nuevo_frame = Frame_ranking(self.root, tipo = "blitz3")
            nuevo_frame.pack()
            self.forget()
            
        self.blitz3 = ttk.Button(self, text="Blitz 3", width=20, command=blitz3, style="secondary.TButton")
        self.blitz3.grid(row=1, column=0, columnspan=3, pady=5)
        
        def blitz5():
            if self.tipo == "Registro":
                nuevo_frame = Frame_registro(self.root, tipo = "blitz5")
            elif self.tipo == "Ranking":
                nuevo_frame = Frame_ranking(self.root, tipo = "blitz5")
            nuevo_frame.pack()
            self.forget()

        self.blitz5 = ttk.Button(self, text="Blitz 5", width=20, command=blitz5, style="secondary.TButton")
        self.blitz5.grid(row=2, column=0, columnspan=3, pady=5)
        
        def classic10():
            if self.tipo == "Registro":
                nuevo_frame = Frame_registro(self.root, tipo = "classic10")
            elif self.tipo == "Ranking":
                nuevo_frame = Frame_ranking(self.root, tipo = "classic10")
            nuevo_frame.pack()
            self.forget()
        
        self.classic10 = ttk.Button(self, text="Classic 10", width=20, command=classic10, style="secondary.TButton")
        self.classic10.grid(row=3, column=0, columnspan=3, pady=5)
        
        def classic30():
            if self.tipo == "Registro":
                nuevo_frame = Frame_registro(self.root, tipo = "classic30")
            elif self.tipo == "Ranking":
                nuevo_frame = Frame_ranking(self.root, tipo = "classic30")
            nuevo_frame.pack()
            self.forget()
            
        self.classic30 = ttk.Button(self, text="Classic 30", width=20, command=classic30, style="secondary.TButton")
        self.classic30.grid(row=4, column=0, columnspan=3, pady=5)
        
        #Boton de regreso
        def boton_regreso():
            nuevo_frame = Frame_inicio(self.root)
            nuevo_frame.pack()
            self.forget()
        
        self.boton_regreso = ttk.Button(self, text='Regresar', command=boton_regreso, style="danger.TButton", width=8)
        self.boton_regreso.grid(row=5, column=2, pady=(5,20))

class Frame_registro(FrameTematico):
    def __init__(self, root = None, tipo = None):
        super().__init__(root)
        self.root = root
        self.tipo = tipo
        self.pack()
        self.campo_registro()
        self.tabla_registro()
    
    def deseleccionar_combobox(self, event):
        self.focus_set()
        self.dummy_label.focus_set()
    
    def ganador_combobox(self, event):
        self.focus_set()
        self.dummy_label.focus_set()
        seleccion = self.sel_resultado.get()
        if seleccion == "Blancas":
            self.jugador_blancas.configure(style="victoria.secondary.TCombobox")
            self.jugador_negras.configure(style="derrota.secondary.TCombobox")
        elif seleccion == "Negras":
            self.jugador_blancas.configure(style="derrota.secondary.TCombobox")
            self.jugador_negras.configure(style="victoria.secondary.TCombobox")
        elif seleccion == "Tablas":
            self.jugador_blancas.configure(style="empate.secondary.TCombobox")
            self.jugador_negras.configure(style="empate.secondary.TCombobox")
    
    def campo_registro(self):
        
        #Labels:
        if self.tipo == "blitz3":
            texto = "Registro de Blitz 3"
        elif self.tipo == "blitz5":
            texto = "Registro de Blitz 5"
        elif self.tipo == "classic10":
            texto = "Registro de Classic 10"
        elif self.tipo == "classic30":
            texto = "Registro de Classic 30"
        else:
            nuevo_frame = Frame_inicio(self.root)
            nuevo_frame.pack()
            self.forget()
            texto = ""
        
        #Dummy labels
        self.dummy_label = ttk.Label(self, text="")
        self.dummy_label.grid(row=0, column=0)
        
        self.label_titulo = ttk.Label(self, text=texto, style="Titulo.TLabel")
        self.label_titulo.grid(row=0, column=0, columnspan=5, padx=30, pady=(20,10))
        
        self.blancas_titulo = ttk.Label(self, text="Blancas", style="SubTitulo.TLabel")
        self.blancas_titulo.grid(row=1, column=1, padx=(10,0))
        
        self.negras_titulo = ttk.Label(self, text="Negras", style="SubTitulo.TLabel")
        self.negras_titulo.grid(row=1, column=3, padx=(0,10))
        
        self.blancas_image = Image.open("img/ch-rey-blanco.png")
        self.blancas_image = self.blancas_image.resize((45,45)) 
        self.blancas_photo = ImageTk.PhotoImage(self.blancas_image)
        self.blancas = ttk.Label(self, image=self.blancas_photo)
        self.blancas.grid(row=2, column=0, padx=(20,0))
        
        self.vs_image = Image.open("img/ch-vs.png")
        self.vs_image = self.vs_image.resize((40,40)) 
        self.vs_photo = ImageTk.PhotoImage(self.vs_image)
        self.vs = ttk.Label(self, image=self.vs_photo)
        self.vs.grid(row=2, column=2)
        
        self.nergas_image = Image.open("img/ch-rey-negro.png")
        self.nergas_image = self.nergas_image.resize((45,45)) 
        self.negras_photo = ImageTk.PhotoImage(self.nergas_image)
        self.negras = ttk.Label(self, image=self.negras_photo)
        self.negras.grid(row=2, column=4, pady=5, padx=(0,20))
        
        self.lista_jugadores = listar_jugadores(tipo=self.tipo)
        self.nombre_a_id = {jugador[1]: jugador[0] for jugador in self.lista_jugadores}
        nombres = list(self.nombre_a_id.keys())

        self.var_blancas = tk.StringVar(self)
        self.jugador_blancas = ttk.Combobox(self, textvariable=self.var_blancas, values=nombres, state='readonly', justify='center', width=10, style="secondary.TCombobox", font=('Ms Trebuchet', 12))
        self.jugador_blancas.grid(row=2, column=1, padx=(5,15), pady=5 , sticky='e')
        self.jugador_blancas.bind("<<ComboboxSelected>>", self.deseleccionar_combobox)
        
        self.var_negras = tk.StringVar(self)
        self.jugador_negras = ttk.Combobox(self, textvariable=self.var_negras, values=nombres, state='readonly', justify='center', width=10, style="secondary.TCombobox", font=('Ms Trebuchet', 12))
        self.jugador_negras.grid(row=2, column=3, padx=(15,5), pady=5, sticky='w')
        self.jugador_negras.bind("<<ComboboxSelected>>", self.deseleccionar_combobox)
        
        contenedor_resultado = ttk.Frame(self)
        contenedor_resultado.grid(row=3, column=0, columnspan=5, padx=5)
        
        self.victoria = ttk.Label(contenedor_resultado, text="Resultado:", style="SubTitulo.TLabel")
        self.victoria.grid(row=0, column=0, pady=15, padx=7, sticky='e')
        
        vic_resultados = ["Blancas", "Negras", "Tablas"]
        self.var_resultado= tk.StringVar(self)
        self.sel_resultado = ttk.Combobox(contenedor_resultado, textvariable=self.var_resultado, values=vic_resultados, state='readonly', justify='center', width=10, style="secondary.TCombobox", font=('Ms Trebuchet', 12))
        self.sel_resultado.grid(row=0, column=1, pady=15, padx=7, sticky='w')
        self.sel_resultado.bind("<<ComboboxSelected>>", self.ganador_combobox)
        
        #Boton de registro
        def boton_registrar():
            id_blancas = self.nombre_a_id.get(self.var_blancas.get())
            id_negras = self.nombre_a_id.get(self.var_negras.get())
            resultado = self.var_resultado.get()
            if id_blancas is not None and id_negras is not None and resultado is not None:
                if id_blancas == id_negras:
                    messagebox.showwarning("Advertencia", "Un jugador no puede enfrentarse a sí mismo")
                else:
                    calcular_elo(id_blancas, id_negras, resultado, tipo=self.tipo)
                    registrar_partida(id_blancas, id_negras, resultado, tipo=self.tipo)
                    self.jugador_blancas.configure(style="secondary.TCombobox")
                    self.jugador_negras.configure(style="secondary.TCombobox")
                    self.var_blancas.set("")
                    self.var_negras.set("")
                    self.var_resultado.set("")
                    self.tabla_registro()
            else:
                messagebox.showwarning("Advertencia", "Faltan completar datos")
        
        self.boton_registrar = ttk.Button(contenedor_resultado, text="Registrar", width=20, command=boton_registrar, style="info.TButton")
        self.boton_registrar.grid(row=1, column=0, padx=15)
        
        #Boton de regreso
        def boton_regreso():
            nuevo_frame = Frame_inicio(self.root)
            nuevo_frame.pack()
            self.forget()
        
        self.boton_regreso = ttk.Button(contenedor_resultado, text="Regresar", width=20, command=boton_regreso, style="dangerous.TButton")
        self.boton_regreso.grid(row=1, column=1, padx=15)
        
        contenedor_botones = ttk.Frame(self)
        contenedor_botones.grid(row=5, column=0, columnspan=5)
        
        #Boton para nuevo jugador
        def boton_nuevo_jugador():
            nuevo_frame = Frame_nuevo_jugador(self.root, tipo=self.tipo)
            nuevo_frame.pack()
            self.forget()
        
        self.boton_nuevo_jugador = ttk.Button(contenedor_botones, text="Nuevo Jugador", width=20, command=boton_nuevo_jugador, style="success.TButton")
        self.boton_nuevo_jugador.grid(row=0, column=0, pady=15, padx=15)
        
        #Boton de historial
        def boton_historial():
            nuevo_frame = Frame_historial(self.root, tipo=self.tipo)
            nuevo_frame.pack()
            self.forget()
        
        self.boton_regreso = ttk.Button(contenedor_botones, text="Ver Historial", width=20, command=boton_historial, style="warning.TButton")
        self.boton_regreso.grid(row=0, column=1, pady=15, padx=15)
    
    def tabla_registro(self):
        self.lista_jugadores = listar_jugadores(tipo=self.tipo)
        self.lista_jugadores.sort(key=lambda jugador: jugador[2])
        contenedor_tabla = ttk.Frame(self)
        contenedor_tabla.grid(row=4, column=0, columnspan=5, padx=20)
        
        separator = ttk.Separator(contenedor_tabla, orient='horizontal')
        separator.grid(row=0, column=0, columnspan=2, pady=15, sticky='ew')
        
        self.tabla = ttk.Treeview(contenedor_tabla,
                                  columns=("Nombre", "Elo", "Partidas", "Victorias", "Racha"),
                                  show='headings',
                                  selectmode="none",
                                  style="secondary.Treeview",
                                  height=6
                                  )
        self.tabla.heading('#1', text="Nombre")
        self.tabla.heading('#2', text="Elo")
        self.tabla.heading('#3', text="Partidas")
        self.tabla.heading('#4', text="Victorias")
        self.tabla.heading('#5', text="Racha")
        
        self.tabla.column('#1', width=130, minwidth=130, stretch=False, anchor="w")
        self.tabla.column('#2', width=70, minwidth=70, stretch=False, anchor='center')
        self.tabla.column('#3', width=70, minwidth=70, stretch=False, anchor='center')
        self.tabla.column('#4', width=70, minwidth=70, stretch=False, anchor='center')
        self.tabla.column('#5', width=60, minwidth=60, stretch=False, anchor='center')
        
        scrollbar = ttk.Scrollbar(contenedor_tabla, orient='vertical', command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        
        self.tabla.grid(row=1, column=0, sticky='nsew')
        scrollbar.grid(row=1, column=1, sticky='ns')
        
        for p in self.lista_jugadores:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4], p[13]))

class Frame_nuevo_jugador(FrameTematico):
    def __init__(self, root = None, tipo = None):
        super().__init__(root)
        self.root = root
        self.tipo = tipo
        self.pack()
        self.campo_nuevo()
        
    def campo_nuevo(self):
        self.titulo = ttk.Label(self, text="Agregar Nuevo Jugador", style="Titulo.TLabel")
        self.titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        def boton_agregar():
            if nombre_existente(tipo=self.tipo, nombre=self.var_nombre_nuevo.get()):
                messagebox.showwarning("Advertencia", "Este jugador ya existe, ingrese otro nombre")
            else:
                jugador_nuevo = Jugador(
                    self.var_nombre_nuevo.get(),
                    800,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                )
                guardar_jugador(jugador_nuevo,tipo=self.tipo)
                nuevo_frame = Frame_registro(self.root, tipo=self.tipo)
                nuevo_frame.pack()
                self.var_nombre_nuevo.set("")
                self.forget()
        
        def boton_cancelar():
            self.var_nombre_nuevo.set("")
            nuevo_frame = Frame_registro(self.root, tipo=self.tipo)
            nuevo_frame.pack()
            self.forget()
        
        self.nombre_label = ttk.Label(self, text="Nombre:", style="SubTitulo.TLabel")
        self.nombre_label.grid(row=1, column=0, padx=5, sticky="e")
        
        self.var_nombre_nuevo = tk.StringVar()
        self.nombre_entry = ttk.Entry(self, justify=tk.LEFT, width=15 ,textvariable=self.var_nombre_nuevo, style="secondary.TEntry")
        self.nombre_entry.grid(row=1, column=1, padx=5, sticky="w")
        self.nombre_entry.focus_set()
        
        self.boton_agregar = ttk.Button(self, text="Agregar", width=20, command=boton_agregar, style="success.TButton")
        self.boton_agregar.grid(row=2, column=0, padx=15, pady=15)

        self.boton_cancelar = ttk.Button(self, text="Cancelar", width=20, command=boton_cancelar, style="danger.TButton")
        self.boton_cancelar.grid(row=2, column=1, padx=15, pady=15)

class Frame_historial(FrameTematico):
    def __init__(self, root = None, tipo = None):
        super().__init__(root)
        self.root = root
        self.tipo = tipo
        self.pack()
        self.campo_historial()
        
    def campo_historial(self):
        if self.tipo == "blitz3":
            texto = "Historial de Blitz 3"
        elif self.tipo == "blitz5":
            texto = "Historial de Blitz 5"
        elif self.tipo == "classic10":
            texto = "Historial de Classic 10"
        elif self.tipo == "classic30":
            texto = "Historial de Classic 30"
        else:
            texto = "Historial General"
        
        self.titulo_historial = ttk.Label(self, text=texto, style="Titulo.TLabel")
        self.titulo_historial.grid(row=0, column=0, columnspan=2, padx=30, pady=(20,10), sticky="ew")
        self.lista_partidas = listar_partidas()
        self.lista_partidas.reverse()
        self.filtro = [p for p in self.lista_partidas if p[1] == self.tipo]
        contenedor_tabla_h = ttk.Frame(self)
        contenedor_tabla_h.grid(row=1, column=0, columnspan=2, padx=20)
        
        if self.tipo is None:
            self.tabla = ttk.Treeview(contenedor_tabla_h,
                                  columns=("Tipo", "Partida", "Resultado", "Fecha"),
                                  show='headings',
                                  selectmode="none",
                                  style="secondary.Treeview",
                                  height=9
                                  )
            
            self.tabla.heading('#1', text="Tipo")
            self.tabla.heading('#2', text="Partida")
            self.tabla.heading('#3', text="Resultado")
            self.tabla.heading('#4', text="Fecha")
            
            self.tabla.column('#1', width=70, minwidth=70, stretch=False, anchor="center")
            self.tabla.column('#2', width=150, minwidth=150, stretch=False, anchor="center")
            self.tabla.column('#3', width=100, minwidth=100, stretch=False, anchor='center')
            self.tabla.column('#4', width=100, minwidth=100, stretch=False, anchor='center')
            
            scrollbar = ttk.Scrollbar(contenedor_tabla_h, orient='vertical', command=self.tabla.yview)
            self.tabla.configure(yscrollcommand=scrollbar.set)
            
            for p in self.lista_partidas:
                self.tabla.insert('', 'end', text=p[0], values=(p[1], p[2]+" [B] vs "+p[3]+" [N]", p[4], p[5]))
        else:
            self.tabla = ttk.Treeview(contenedor_tabla_h,
                                  columns=("Partida", "Resultado", "Fecha"),
                                  show='headings',
                                  selectmode="none",
                                  style="secondary.Treeview",
                                  height=9
                                  )
            
            self.tabla.heading('#1', text="Partida")
            self.tabla.heading('#2', text="Resultado")
            self.tabla.heading('#3', text="Fecha")
            
            self.tabla.column('#1', width=150, minwidth=150, stretch=False, anchor="center")
            self.tabla.column('#2', width=100, minwidth=100, stretch=False, anchor='center')
            self.tabla.column('#3', width=100, minwidth=100, stretch=False, anchor='center')
            
            scrollbar = ttk.Scrollbar(contenedor_tabla_h, orient='vertical', command=self.tabla.yview)
            self.tabla.configure(yscrollcommand=scrollbar.set)
            for p in self.filtro:
                self.tabla.insert('', 'end', text=p[0], values=(p[2]+" [B] vs "+p[3]+" [N]", p[4], p[5]))
        
        self.tabla.grid(row=1, column=0, sticky='nsew')
        scrollbar.grid(row=1, column=1, sticky='ns')
        
        def boton_regreso():
            if self.tipo == None:
                nuevo_frame = Frame_inicio(self.root)
                nuevo_frame.pack()
            else:
                nuevo_frame = Frame_registro(self.root, tipo=self.tipo)
                nuevo_frame.pack()
            self.forget()
        
        self.boton_regreso = ttk.Button(self, text="Regresar", width=20, command=boton_regreso, style="dangerous.TButton")
        self.boton_regreso.grid(row=2, column=1, padx=15, pady=15, sticky="e")

class Frame_ranking(FrameTematico):
    def __init__(self, root = None, tipo = None):
        super().__init__(root)
        self.root = root
        self.tipo = tipo
        self.pack()
        self.campo_ranking()
        
    def campo_ranking(self):
        #Labels:
        if self.tipo == "blitz3":
            texto = "Ranking de Blitz 3"
        elif self.tipo == "blitz5":
            texto = "Ranking de Blitz 5"
        elif self.tipo == "classic10":
            texto = "Ranking de Classic 10"
        elif self.tipo == "classic30":
            texto = "Ranking de Classic 30"
        else:
            nuevo_frame = Frame_inicio(self.root)
            nuevo_frame.pack()
            self.forget()
            texto = ""
            
        self.ranking_titulo = ttk.Label(self, text=texto, style="Titulo.TLabel")
        self.ranking_titulo.grid(row=0, column=0, columnspan=2, padx=30, pady=(20,10))
        
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0, columnspan=2, padx=10)
        
        tab_elo = Frame_pestaña(self, tipo=self.tipo, filtro = 2, encabezado="Elo")
        self.notebook.add(tab_elo, text="Elo")
        
        tab_victorias = Frame_pestaña(self, tipo=self.tipo, filtro = 4, encabezado="Victorias")
        self.notebook.add(tab_victorias, text="Victorias")
        
        tab_vic_blancas = Frame_pestaña(self, tipo=self.tipo, filtro = 5, encabezado="V. Blancas")
        self.notebook.add(tab_vic_blancas, text="V. Blancas")
        
        tab_vic_negras = Frame_pestaña(self, tipo=self.tipo, filtro = 6, encabezado="V. Negras")
        self.notebook.add(tab_vic_negras, text="V. Negras")
        
        def boton_regreso():
            nuevo_frame = Frame_inicio(self.root)
            nuevo_frame.pack()
            self.forget()
        
        self.boton_regreso = ttk.Button(self, text="Regresar", width=20, command=boton_regreso, style="dangerous.TButton")
        self.boton_regreso.grid(row=2, column=1, padx=15, pady=15, sticky="e")

class Frame_pestaña(FrameTematico):
    def __init__(self, root = None, tipo = None, filtro = None, encabezado = None):
        super().__init__(root)
        self.root = root
        self.tipo = tipo
        self.filtro = filtro
        self.encabezado = encabezado
        self.grid(sticky="nsew")
        self.campo_pestaña()
    def campo_pestaña(self):
        self.lista_jugadores = listar_jugadores(tipo=self.tipo)
        self.lista_jugadores.sort(key=lambda jugador: jugador[self.filtro])
        self.lista_jugadores.reverse()

        nombres = [jugador[1] for jugador in self.lista_jugadores]
        puntajes = [jugador[self.filtro] for jugador in self.lista_jugadores]
        
        while len(nombres) < 5:
            nombres.append("N/A")

        while len(puntajes) < 5:
            puntajes.append("-")
        
        self.puesto_encabezado = ttk.Label(self, text="Puesto", style="SubTitulo.TLabel", width=7)
        self.puesto_encabezado.grid(row=0, column=0, padx=25, pady=10)
        self.nombre_encabezado = ttk.Label(self, text="Jugador", style="SubTitulo.TLabel",width=13)
        self.nombre_encabezado.grid(row=0, column=1, pady=10)
        self.puntaje_encabezado = ttk.Label(self, text=self.encabezado, style="SubTitulo.TLabel", width=10)
        self.puntaje_encabezado.grid(row=0, column=2, padx=25, pady=10)
        
        self.splitter0 = ttk.Separator(self, orient="horizontal")
        self.splitter0.grid(row=1, column=0, columnspan=3, padx=15, sticky='ew')
        
        self.rey_image = Image.open("img/ch-rey-blanco.png")
        self.rey_image = self.rey_image.resize((50,50)) 
        self.rey_photo = ImageTk.PhotoImage(self.rey_image)
        self.rey = ttk.Label(self, image=self.rey_photo)
        self.rey.grid(row=2, column=0, pady=2, sticky="ew")
        
        self.label_rey_nombre = ttk.Label(self, text=nombres[0], style="SubSubTitulo.TLabel")
        self.label_rey_nombre.grid(row=2, column=1, pady=2, sticky="ew")
        
        self.label_rey_puntaje = ttk.Label(self, text=puntajes[0], style="SubSubTitulo.TLabel")
        self.label_rey_puntaje.grid(row=2, column=2, pady=2, sticky="ew")
        
        self.splitter1 = ttk.Separator(self, orient="horizontal")
        self.splitter1.grid(row=3, column=0, columnspan=3, padx=15, sticky='ew')
        
        self.torre_image = Image.open("img/ch-torre-blanco.png")
        self.torre_image = self.torre_image.resize((45,45)) 
        self.torre_photo = ImageTk.PhotoImage(self.torre_image)
        self.torre = ttk.Label(self, image=self.torre_photo)
        self.torre.grid(row=4, column=0, pady=2, sticky="ew")
        
        self.label_torre_nombre = ttk.Label(self, text=nombres[1], style="SubSubTitulo.TLabel")
        self.label_torre_nombre.grid(row=4, column=1, pady=2, sticky="ew")
        
        self.label_torre_puntaje = ttk.Label(self, text=puntajes[1], style="SubSubTitulo.TLabel")
        self.label_torre_puntaje.grid(row=4, column=2, pady=2, sticky="ew")
        
        self.splitter2 = ttk.Separator(self, orient="horizontal")
        self.splitter2.grid(row=5, column=0, columnspan=3, padx=15, sticky='ew')
        
        self.alfin_image = Image.open("img/ch-alfil-blanco.png")
        self.alfin_image = self.alfin_image.resize((50,50)) 
        self.alfin_photo = ImageTk.PhotoImage(self.alfin_image)
        self.alfin = ttk.Label(self, image=self.alfin_photo)
        self.alfin.grid(row=6, column=0, pady=2, sticky="ew")
        
        self.label_alfin_nombre = ttk.Label(self, text=nombres[2], style="SubSubTitulo.TLabel")
        self.label_alfin_nombre.grid(row=6, column=1, pady=2, sticky="ew")
        
        self.label_alfin_puntaje = ttk.Label(self, text=puntajes[2], style="SubSubTitulo.TLabel")
        self.label_alfin_puntaje.grid(row=6, column=2, pady=2, sticky="ew")
        
        self.splitter3 = ttk.Separator(self, orient="horizontal")
        self.splitter3.grid(row=7, column=0, columnspan=3, padx=15, sticky='ew')
        
        self.caballo_image = Image.open("img/ch-caballo-blanco.png")
        self.caballo_image = self.caballo_image.resize((45,45)) 
        self.caballo_photo = ImageTk.PhotoImage(self.caballo_image)
        self.caballo = ttk.Label(self, image=self.caballo_photo)
        self.caballo.grid(row=8, column=0, pady=2, sticky="ew")
        
        self.label_caballo_nombre = ttk.Label(self, text=nombres[3], style="SubSubTitulo.TLabel")
        self.label_caballo_nombre.grid(row=8, column=1, pady=2, sticky="ew")
        
        self.label_caballo_puntaje = ttk.Label(self, text=puntajes[3], style="SubSubTitulo.TLabel")
        self.label_caballo_puntaje.grid(row=8, column=2, pady=2, sticky="ew")
        
        self.splitter4 = ttk.Separator(self, orient="horizontal")
        self.splitter4.grid(row=9, column=0, columnspan=3, padx=15, sticky='ew')
        
        self.peon_image = Image.open("img/ch-peon-blanco.png")
        self.peon_image = self.peon_image.resize((45,45)) 
        self.peon_photo = ImageTk.PhotoImage(self.peon_image)
        self.peon = ttk.Label(self, image=self.peon_photo)
        self.peon.grid(row=10, column=0, pady=2, sticky="ew")
        
        self.label_peon_nombre = ttk.Label(self, text=nombres[4], style="SubSubTitulo.TLabel")
        self.label_peon_nombre.grid(row=10, column=1, pady=2, sticky="ew")
        
        self.label_peon_puntaje = ttk.Label(self, text=puntajes[4], style="SubSubTitulo.TLabel")
        self.label_peon_puntaje.grid(row=10, column=2, pady=2, sticky="ew")

class Frame_torneo(FrameTematico):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.campo_torneo()
        
    def campo_torneo(self):
        #Labels:
        self.label_titulo = ttk.Label(self, text="Funcionalidad en Desarrollo", style="Titulo.danger.TLabel")
        self.label_titulo.grid(row=0, column=0, columnspan=2, padx=30, pady=(20,5))
        
        self.mono_image = Image.open("img/ch-mono.png")
        self.mono_image = self.mono_image.resize((330,330)) 
        self.mono_photo = ImageTk.PhotoImage(self.mono_image)
        self.mono = ttk.Label(self, image=self.mono_photo)
        self.mono.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.subtitulo_label = ttk.Label(self, text="Monos Trabajando", style="SubTitulo.TLabel")
        self.subtitulo_label.grid(row=2, column=0, columnspan=2, pady=(0,10))
        
        #Boton de regreso
        def boton_regreso():
            nuevo_frame = Frame_inicio(root=self.root)
            nuevo_frame.pack()
            self.forget()
        
        self.boton_regreso = ttk.Button(self, text="Regresar", width=20, command=boton_regreso, style="dangerous.TButton")
        self.boton_regreso.grid(row=3, column=1, pady=(5,20))

def calcular_elo(id_blanca, id_negra, resultado, tipo):
    datos_blanca = obtener_jugador(id_blanca, tipo)
    datos_negra = obtener_jugador(id_negra, tipo)
    R1 = datos_blanca[0][2]
    R2 = datos_negra[0][2]
    E1 = 1 / (1 + 10 ** ((R2 - R1) / 400))
    E2 = 1 / (1 + 10 ** ((R1 - R2) / 400))
    if resultado == "Blancas":
        S1, S2 = 1, 0
        R1_new = round(R1 + 20 * (S1 - E1),2)
        R2_new = round(R2 + 20 * (S2 - E2),2)
        nuevos_datos_blancas = Jugador(
            datos_blanca[0][1],
            R1_new,
            datos_blanca[0][3] + 1,
            datos_blanca[0][4] + 1,
            datos_blanca[0][5] + 1,
            datos_blanca[0][6],
            datos_blanca[0][7],
            datos_blanca[0][8],
            datos_blanca[0][9],
            datos_blanca[0][10],
            datos_blanca[0][11],
            datos_blanca[0][12],
            datos_blanca[0][13] + 1
        )
        actualizar_jugador(nuevos_datos_blancas, id_blanca, tipo)
        nuevos_datos_negras = Jugador(
            datos_negra[0][1],
            R2_new,
            datos_negra[0][3] + 1,
            datos_negra[0][4],
            datos_negra[0][5],
            datos_negra[0][6],
            datos_negra[0][7] + 1,
            datos_negra[0][8],
            datos_negra[0][9] + 1,
            datos_negra[0][10],
            datos_negra[0][11],
            datos_negra[0][12],
            0
        )
        actualizar_jugador(nuevos_datos_negras, id_negra, tipo)
        
    elif resultado == "Tablas":
        S1, S2 = 0.5, 0.5
        R1_new = round(R1 + 20 * (S1 - E1),2)
        R2_new = round(R2 + 20 * (S2 - E2),2)
        nuevos_datos_blancas = Jugador(
            datos_blanca[0][1],
            R1_new,
            datos_blanca[0][3] + 1,
            datos_blanca[0][4],
            datos_blanca[0][5],
            datos_blanca[0][6],
            datos_blanca[0][7],
            datos_blanca[0][8],
            datos_blanca[0][9],
            datos_blanca[0][10] + 1,
            datos_blanca[0][11] + 1,
            datos_blanca[0][12],
            datos_blanca[0][13]
        )
        actualizar_jugador(nuevos_datos_blancas, id_blanca, tipo)
        nuevos_datos_negras = Jugador(
            datos_negra[0][1],
            R2_new,
            datos_negra[0][3] + 1,
            datos_negra[0][4],
            datos_negra[0][5],
            datos_negra[0][6],
            datos_negra[0][7],
            datos_negra[0][8],
            datos_negra[0][9],
            datos_negra[0][10] + 1,
            datos_negra[0][11],
            datos_negra[0][12] + 1,
            datos_negra[0][13]
        )
        actualizar_jugador(nuevos_datos_negras, id_negra, tipo)
    elif resultado == "Negras":
        S1, S2 = 0, 1
        R1_new = round(R1 + 20 * (S1 - E1),2)
        R2_new = round(R2 + 20 * (S2 - E2),2)
        nuevos_datos_blancas = Jugador(
            datos_blanca[0][1],
            R1_new,
            datos_blanca[0][3] + 1,
            datos_blanca[0][4],
            datos_blanca[0][5],
            datos_blanca[0][6],
            datos_blanca[0][7] + 1,
            datos_blanca[0][8] + 1,
            datos_blanca[0][9],
            datos_blanca[0][10],
            datos_blanca[0][11],
            datos_blanca[0][12],
            0
        )
        actualizar_jugador(nuevos_datos_blancas, id_blanca, tipo)
        nuevos_datos_negras = Jugador(
            datos_negra[0][1],
            R2_new,
            datos_negra[0][3] + 1,
            datos_negra[0][4] + 1,
            datos_negra[0][5],
            datos_negra[0][6] + 1,
            datos_negra[0][7],
            datos_negra[0][8],
            datos_negra[0][9],
            datos_negra[0][10],
            datos_negra[0][11],
            datos_negra[0][12],
            datos_negra[0][13] + 1
        )
        actualizar_jugador(nuevos_datos_negras, id_negra, tipo)

def registrar_partida(id_blanca, id_negra, resultado, tipo):
    datos_blanca = obtener_jugador(id_blanca, tipo)
    datos_negra = obtener_jugador(id_negra, tipo)
    nueva_partida = Partida(
        tipo,
        datos_blanca[0][1],
        datos_negra[0][1],
        resultado,
        datetime.datetime.now().strftime('%Y-%m-%d')
    )
    guardar_partida(nueva_partida)
