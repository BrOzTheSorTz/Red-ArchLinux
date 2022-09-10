#!/usr/bin/env python3
import sys
import subprocess

def verificar_conexion():
    
    try:
        subprocess.run(["ping", "8.8.8.8"],timeout = 3)
    except Exception:
        return True 
    return False


