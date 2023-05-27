import ctypes
from ctypes.util import find_library
library = ctypes.cdll.LoadLibrary(find_library("multiplicador"))
print(library.multiplicar_por_100)
pos = library.multiplicar_por_100(3)
#x = ctypes.cast(addr, ctypes.POINTER(ctypes.c_int)).contents
#x = ctypes.cast(addr + 4, ctypes.POINTER(ctypes.c_int)).contents