import wmi

f = wmi.WMI()
for process in f.Win32_Process():
    print(f'{process.ProcessId:<10}poop')
