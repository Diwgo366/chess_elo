import sqlite3
import os

class ConexionBD:
    def __init__(self, tipo = None):
        if not os.path.exists('database/'):
            os.makedirs('database/')
        self.base_datos = f'database/{tipo}.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
        
class ConexionHistorial:
    def __init__(self):
        if not os.path.exists('database/'):
            os.makedirs('database/')
        self.base_datos = f'database/historial.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()