import wmi
f = wmi.WMI()

for process in f.Win32_Process():
 #   print(process.name)
    if process.name == 'notepad.exe':
        process.Terminate()
        
