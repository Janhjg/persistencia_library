import pytest
from Persistencia_datos import *
import os

def test_read():
    def test_archivo_no_existe():
        # ARCHIVO QUE NO EXISTE LANZA ERROR
        with pytest.raises(FileNotFoundError):
            read("no_existe.json") 
    
    def archivo_valido():
        # Lee un archivo Json correcto
        archivo = "test_temp.json"
        datos = {"nombre": "Test", "saldo": 100}
        
        with open(archivo, 'w') as f:
            json.dump(datos, f)
        try:
        # 2. Leer con la función
            resultado = read(archivo)
        
        # 3. Verificar
            assert resultado == datos
        finally:
            os.remove(archivo)
            
def test_write():
    def test_write_archivo_con_datos():
        # Escribe datos en un archivo
        pass 
    
def test_update():
    def test_modifica_archivo():
        # Actualiza archivo existente
        pass

def test_clear():
    def test_limpia_archivo():
        # Testea que se limpie todo el archivo
        pass

def test_delete():
    def test_elimina_archivo():
        # Verifica que se limpie el archivo
        pass
    def test_archivo_no_existe():
        # ELIMINAR ARCHIVO QUE NO EXISTA LANZA ERROR
        pass