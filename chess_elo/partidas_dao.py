from .conexion_db import ConexionBD, ConexionHistorial

def crear_tabla_partidas():
    tipos = ["blitz3", "blitz5", "classic10", "classic30"]
    for tipo in tipos:
        conexion = ConexionBD(tipo = tipo)
        
        sql = '''
        CREATE TABLE IF NOT EXISTS jugadores (
            id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100),
            elo INTEGER,
            partidas INTEGER,
            vic_acum INTEGER,
            vic_blancas INTEGER,
            vic_negras INTEGER,
            der_acum INTEGER,
            der_blancas INTEGER,
            der_negras INTEGER,
            tab_acum INTEGER,
            tab_blancas INTEGER,
            tab_negras INTEGER,
            racha INTEGER
        )
        '''
        try:
            conexion.cursor.execute(sql)
        except:
            pass
        finally:
            conexion.cerrar()

def borrar_tabla_partidas():
    tipos = ["blitz3", "blitz5", "classic10", "classic30"]
    for tipo in tipos:
        conexion = ConexionBD(tipo=tipo)
        
        sql = 'DROP TABLE IF EXISTS jugadores'
        
        try:
            conexion.cursor.execute(sql)
        except:
            pass
        finally:
            conexion.cerrar()

def crear_tabla_historial():
    conexion = ConexionHistorial()
    sql = '''
    CREATE TABLE IF NOT EXISTS partidas (
        id_partida INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo VARCHAR(30),
        blancas VARCHAR(100),
        negras VARCHAR(100),
        resultado VARCHAR(100),
        fecha DATE
    )
    '''
    try:
        conexion.cursor.execute(sql)
    except:
        pass
    finally:
        conexion.cerrar()

def borrar_tabla_historial():
    conexion = ConexionHistorial()
        
    sql = 'DROP TABLE IF EXISTS partidas'
    
    try:
        conexion.cursor.execute(sql)
    except:
        pass
    finally:
        conexion.cerrar()

class Jugador:
    def __init__(self, nombre, elo, partidas, vic_acum, vic_blancas, vic_negras, der_acum, der_blancas,
                 der_negras, tab_acum, tab_blancas, tab_negras, racha):
        self.id_jugador = None
        self.nombre = nombre
        self.elo = elo
        self.partidas = partidas
        self.vic_acum = vic_acum
        self.vic_blancas = vic_blancas
        self.vic_negras = vic_negras
        self.der_acum = der_acum
        self.der_blancas = der_blancas
        self.der_negras = der_negras
        self.tab_acum = tab_acum
        self.tab_blancas = tab_blancas
        self.tab_negras = tab_negras
        self.racha = racha
    
    def __str__(self):
        return (f"Jugador: {self.nombre}\n"
                f"ELO: {self.elo}\n"
                f"Partidas: {self.partidas}\n"
                f"Victorias Acumuladas: {self.vic_acum}\n"
                f"Victorias Blancas: {self.vic_blancas}\n"
                f"Victorias Negras: {self.vic_negras}\n"
                f"Derrotas Acumuladas: {self.der_acum}\n"
                f"Derrotas Blancas: {self.der_blancas}\n"
                f"Derrotas Negras: {self.der_negras}\n"
                f"Tablas Acumuladas: {self.tab_acum}\n"
                f"Tablas Blancas: {self.tab_blancas}\n"
                f"Tablas Negras: {self.tab_negras}\n"
                f"Racha: {self.racha}"
                )

class Partida:
    def __init__(self, tipo, blancas, negras, resultado, fecha):
        self.id_partida = None
        self.tipo = tipo
        self.blancas = blancas
        self.negras = negras
        self.resultado = resultado
        self.fecha = fecha
    
    def __str__(self):
        return (f"Tipo: {self.tipo}\n"
                f"Blancas: {self.blancas}\n"
                f"Negras: {self.negras}\n"
                f"Resultado: {self.resultado}\n"
                f"Fecha: {self.fecha}"
                )

def guardar_jugador(jugador, tipo):
    conexion = ConexionBD(tipo=tipo)
    sql = f"""INSERT INTO jugadores(nombre, elo, partidas, vic_acum, vic_blancas, vic_negras, der_acum, der_blancas, der_negras, tab_acum, tab_blancas, tab_negras, racha)
    VALUES('{jugador.nombre}','{jugador.elo}','{jugador.partidas}','{jugador.vic_acum}','{jugador.vic_blancas}','{jugador.vic_negras}','{jugador.der_acum}','{jugador.der_blancas}','{jugador.der_negras}','{jugador.tab_acum}','{jugador.tab_blancas}','{jugador.tab_negras}','{jugador.racha}')
    """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        crear_tabla_partidas()
        conexion.cursor.execute(sql)
        conexion.cerrar()

def guardar_partida(partida):
    conexion = ConexionHistorial()
    sql = f"""INSERT INTO partidas(tipo, blancas, negras, resultado, fecha)
    VALUES('{partida.tipo}','{partida.blancas}','{partida.negras}','{partida.resultado}','{partida.fecha}')
    """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        crear_tabla_partidas()
        conexion.cursor.execute(sql)
        conexion.cerrar()

def listar_jugadores(tipo):
    conexion = ConexionBD(tipo=tipo)
    
    lista_jugadores = []
    sql = 'SELECT * FROM jugadores'
    
    try:
        conexion.cursor.execute(sql)
        lista_jugadores = conexion.cursor.fetchall()
    except:
        pass
    finally:
        conexion.cerrar()
        
    return lista_jugadores

def listar_partidas():
    conexion = ConexionHistorial()
    
    lista_partidas = []
    sql = 'SELECT * FROM partidas'
    
    try:
        conexion.cursor.execute(sql)
        lista_partidas = conexion.cursor.fetchall()
    except:
        pass
    finally:
        conexion.cerrar()
        
    return lista_partidas

def obtener_jugador(id_jugador, tipo):
    conexion = ConexionBD(tipo=tipo)
    
    sql = f'SELECT * FROM jugadores WHERE id_jugador = {id_jugador}'
    datos = []
    try:
        conexion.cursor.execute(sql)
        datos = conexion.cursor.fetchall()
    except:
        pass
    finally:
        conexion.cerrar()
    return datos

def actualizar_jugador(jugador, id_jugador, tipo):
    conexion = ConexionBD(tipo=tipo)
    sql = f"""UPDATE jugadores
    SET elo = '{jugador.elo}',
    partidas = '{jugador.partidas}',
    vic_acum = '{jugador.vic_acum}',
    vic_blancas = '{jugador.vic_blancas}',
    vic_negras = '{jugador.vic_negras}',
    der_acum = '{jugador.der_acum}',
    der_blancas = '{jugador.der_blancas}',
    der_negras = '{jugador.der_negras}',
    tab_acum = '{jugador.tab_acum}',
    tab_blancas = '{jugador.tab_blancas}',
    tab_negras = '{jugador.tab_negras}',
    racha = '{jugador.racha}'
    WHERE id_jugador = {id_jugador}
    """
    
    try:
        conexion.cursor.execute(sql)
    except:
        pass
    finally:
        conexion.cerrar()

def nombre_existente(nombre, tipo):
    conexion = ConexionBD(tipo=tipo)
    
    sql = f"SELECT COUNT(*) FROM jugadores WHERE nombre = '{nombre}'"
    
    try:
        conexion.cursor.execute(sql)
        existe = conexion.cursor.fetchone()[0] > 0
    except:
        existe = False 
    finally:
        conexion.cerrar()
    return existe