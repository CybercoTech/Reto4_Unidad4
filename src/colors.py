import os 

os.system('')


clr_error = '\033[31m' 
clr_exito = '\033[32m'
clr_alerta = '\033[33m'
clr_reset = '\033[0m'

def print_error(mensaje: str) -> None:
    print(f"{clr_error}{mensaje}{clr_reset}")

def print_exito(mensaje: str) -> None:
    print(f"{clr_exito}{mensaje}{clr_reset}")

def print_alerta(mensaje: str) -> None:
    print(f"{clr_alerta}{mensaje}{clr_reset}")

def print_azul(texto):
    print(f"\033[94m{texto}\033[0m")

