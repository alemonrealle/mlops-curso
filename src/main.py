
""" 
MLOps - Tema 1: Introducción 
Script de verificación del entorno 
""" 
 
import sys 
import platform 
 
def verificar_entorno(): 
    print("=" * 40) 
    print("  MLOps Curso — Verificación del entorno") 
    print("=" * 40) 
    print(f"Python:  {sys.version.split()[0]}") 
    print(f"Sistema: {platform.system()} {platform.release()}") 
    print() 
 
    librerias = ["numpy", "pandas", "matplotlib"] 
    print("Librerías instaladas:") 
    for lib in librerias: 
        try: 
            mod = __import__(lib) 
            print(f"  OK  {lib} {mod.__version__}") 
        except ImportError: 
            print(f"  --  {lib} NO instalado") 
    print() 
    print("Entorno listo para MLOps.") 
 
if __name__ == "__main__": 
    verificar_entorno() 