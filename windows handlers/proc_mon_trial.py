import wmi

c = wmi.WMI()
proc_watcher = c.WIN32_Process.watch_for('creation')
def log(text):
    fd = open("proc_mon.csv" , "w+")
    fd.write("{}\r\n".format (text))
    fd.close()

log("Time,User,Executable,CommandLine,PID,Parent PID,Privileges")
    
while True:
    try:
        new_proc = proc_watcher()
        proc_owner = new_proc.GetOwner()
        proc_owner = (proc_owner[0] , proc_owner[2])
        create_date = new_proc.CreationDate
        cmd = new_proc.CommandLine
        exe = new_proc.ExecutablePath
        pid = new_proc.ProcessId
        parent_pid = new_proc.ParentProcessId
        priviledge = "N/A"
        mess = "date: {}, owner: {}, exe: {}, cmd: {}, pid: {}, parent_pid: {}, priv: {}\r\n".format(create_date,
proc_owner, exe, cmd, pid, parent_pid, priviledge)
        log(mess)
        print(mess)
    except Exception as e:
        print(e)
        break
