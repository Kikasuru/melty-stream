from ctypes import *
from ctypes.wintypes import *
import psutil # Not a default module, you'll need to install this.
import sys

# No idea what this stuff does, but it works.
STRLEN = 1
PROCESS_VM_READ = 0x0010

k32 = WinDLL('kernel32')
k32.OpenProcess.argtypes = DWORD,BOOL,DWORD
k32.OpenProcess.restype = HANDLE
k32.ReadProcessMemory.argtypes = HANDLE,LPVOID,LPVOID,c_size_t,POINTER(c_size_t)
k32.ReadProcessMemory.restype = BOOL

# Melty Blood executable name.
meltyexename = "MBAA.exe"

# Find the PID of Melty Blood
def getpid():
    for proc in psutil.process_iter():
        if proc.name() == meltyexename:
            return proc.pid

PROCESS_ID = None
process = None

# Make a meltyFind function.
def meltyFind():
    global PROCESS_ID,process

    # Get Melty's PID
    PROCESS_ID = getpid()

    if PROCESS_ID == None:
        # If no process was found, return false.
        return False
    else:
        print("Melty Blood found! PID: "+str(PROCESS_ID))

        # Define the process.
        process = k32.OpenProcess(PROCESS_VM_READ, 0, PROCESS_ID)

        return True

# Create a buffer for the read function.
buf = create_string_buffer(STRLEN)
s = c_size_t()

# Define a read function.
def read(addr):
    if k32.ReadProcessMemory(process, addr, buf, STRLEN, byref(s)):
        return buf.raw
    else: return None
