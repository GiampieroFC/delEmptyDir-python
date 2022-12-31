from __future__ import print_function
import ctypes
from genericpath import isfile
import sys
from pathlib import Path
import time
import os

ruta = 'C:/Users/gferm/OneDrive/Escritorio/DEBERES'


def unlikFile(ruta):
    arr = os.listdir(ruta)
    print('\narr :\n', arr)
    # time.sleep(1.5)
    for a in arr:
        dirfil = os.path.join(ruta, a)
        print("\ndirfil :\n", dirfil)

        if os.path.isdir(dirfil):
            if len(os.listdir(dirfil)) == 0:
                os.rmdir(dirfil)
                print("\nElimina directorio vacío:\n", dirfil)
            else:
                unlikFile(dirfil)
                print("\nEjecuta otra vez con:", dirfil)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    unlikFile(ruta)
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)
    else:  # in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(
            sys.executable), unicode(__file__), None, 1)
