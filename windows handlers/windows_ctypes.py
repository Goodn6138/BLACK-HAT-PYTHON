from ctypes import *
import numpy as np

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi

def get_current_p():
#Get handle of the fore ground window
    hwnd = user32.GetForegroundWindow()
#Find the process ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd , byref(pid))

#Store current process ID
    process_id = pid.value
    print(process_id)
#grab the executable
    exe = create_string_buffer("\x00" ,512)
    h_process = kernel32.OpenProcess((0x400 | 0x10),False , int(pid))
    print(h_process)
    psapi.GetModuleBaseName(h_process, None, byref(exe),512)
#reading the tilte
    wnd_ttl = create_string_buffer(np.array(["\x00"]*512))
    length = user32.GetWindowTextA(hwnd, byref(wnd_ttl), 512)
    return wnd_ttl.value
    
print(get_current_p())
