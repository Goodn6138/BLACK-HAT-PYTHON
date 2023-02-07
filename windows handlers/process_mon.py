from ctypes import *
kernel32 = windll.kernel32
user32 = windll.user32

def get_current_proc():
    #GET HANDLE OF THE FOREGROUND WND
    h_wnd = user32.GetForegroundWindow()

    #GET PID OF THE FOREGROUND WINDOW
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(h_wnd , byref(pid))
    #GET NAME OF THE FOREGROUND WINDOW
    wnd_title = create_string_buffer(b"/x00" * 512)
    user32.GetWindowTextA(h_wnd , byref(wnd_title))
    return wnd_title.value , pid.value

current_pid = ""
while True:
    title , pid = get_current_proc()
    if pid != current_pid:
        print("PID {} TITLE {}".format(pid , title))
        current_pid = pid
    
    
