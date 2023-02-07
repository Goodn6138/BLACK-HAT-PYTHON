from ctypes import *

kernel32 = windll.kernel32
user32 = windll.user32

def gcwnd():
    h_wnd = user32.GetForegroundWindow() #HANDLE YA FOREGROUND WINDOW
    pid = user32.GetWindowThreadProcessId(h_wnd) #PID YA FOR GROUND WINDOW

    wnd_text = create_string_buffer(b'/x00' * 500)
    length = user32.GetWindowTextA(h_wnd , byref(wnd_text))

    return wnd_text.value , pid
