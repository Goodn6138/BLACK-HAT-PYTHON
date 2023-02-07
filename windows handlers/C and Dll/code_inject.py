from ctypes import *

VIRTUAL_MEM = 00
PROCESS_RW = 00
PROCESS_ACCESS_ALL = 00

kernel32 = windll.kernel32
pid = 0
code = 0
code_len = len(code)

#GET HANDLE PROCESS
h_process = kernel32.OpenProcess(PROCESS_ACCESS_ALL, False , int(pid))

#ALLOC MEMORY
arg_addr = kernel32.VirtualAllocEx(h_process, 0, code_len , VIRTUAL_MEM , PROCESS_ACCESS_ALL)

#WRITE INTO MEMORY
written = c_int(0)
kernel32.WriteProcessMemory(h_process ,arg_addr , code , code_len, byref(written))

h_kernel32 = kernel32.GetModuleHandleA("kernl32.dll")
h_loadlib = kernel32.GetProcAddress(h_kernel32 , "LoadLibraryA")

thread_id = c_ulong(0)
if not kernel32.CreateRemoteThread(h_process,
                                  None,
                                  0,
                                  h_loadlib,
                                  arg_addr,
                                  0,
                                  byref(thread_id)):
    print("poop")

