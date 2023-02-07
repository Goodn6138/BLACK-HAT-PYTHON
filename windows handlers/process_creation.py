from __future__ import print_function,unicode_literals
from ctypes import *
from ctypes.wintypes import BYTE,WORD,DWORD,LPWSTR,LPCWSTR,HANDLE,LPVOID,BOOL

LPBYTE = POINTER(BYTE)
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

class STARTUPINFOW(Structure):
    __fields_ = [('cb', DWORD),
                ('lpReserved', LPWSTR),
                ('lpDesktop', LPWSTR),
                ('lpTitle', LPWSTR),
                ('dwX', DWORD),
                ('dwY', DWORD),
                ('dwXSize', DWORD),
                ('dwYSize', DWORD),
                ('dwXCountChars', DWORD),
                ('dwYCountChars', DWORD),
                ('dwFillAttribute',DWORD),
                ('dwFlags', DWORD),
                ('wShowWindow', WORD),
                ('cbReserved2', WORD),
                ('lpReserved2', LPBYTE),
                ('hStdInput', HANDLE),
                ('hStdOutput', HANDLE),
                ('hStdError', HANDLE)]

class PROCESS_INFORMATION(Structure):
    _fields_ = [('hProcess', HANDLE),
                ('hThread', HANDLE),
                ('dwProcessId', DWORD),
                ('dwThreadId', DWORD)]

class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [('nLength', DWORD),
                ('lpSecurityDescriptor', LPVOID),
                ('bInheritHandle', BOOL)]
LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)
LPSTARTUPINFOW = POINTER(STARTUPINFOW)
LPPROCESS_INFORMATION = POINTER(PROCESS_INFORMATION)

kernel32 = WinDLL('kernel32' , use_last_error = True)
kernel32.CreateProcessW.argtypes = (LPCWSTR,LPWSTR,LPSECURITY_ATTRIBUTES,LPSECURITY_ATTRIBUTES,
                                    BOOL,DWORD,LPVOID,LPCWSTR,LPSTARTUPINFOW,LPPROCESS_INFORMATION)
kernel32.restype = BOOL

def load(path_to_exe):
    creation_flags = DEBUG_PROCESS
    startupinfo = STARTUPINFOW()
    processinfo = PROCESS_INFORMATION()
    startupinfo.dwFlags = create_string_buffer(b'0x00' *512)
    startupinfo.wShowWindow = create_string_buffer(b'0x00' *512)
    startupinfo.cb = sizeof(startupinfo)
    if kernel32.CreateProcessW(path_to_exe,None,None,None,False,creation_flags,None,None,byref(startupinfo),byref(processinfo)):
        print('[*] Process launched')
        print('[*] PID: {}'.format(processinfo.dwProcessId))
    else:
        print('[*] Error: 0x{:08x}.'.format(get_last_error()))
load(r"C:/Windows/notepad.exe")
                               
