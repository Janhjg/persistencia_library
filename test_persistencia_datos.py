import pytest
from Persistencia_datos import *
import os

def test_read():
    def test_archivo_no_existe():
        with pytest.raises(FileNotFoundError):
            read("no_existe.json") 
    
    def archivo_valido():
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
    