import subprocess
cmd = 'tasklist /v'
proc = subprocess.getoutput(cmd).split("\n")
file = open("Process_list.txt", "w+")
file.write(str(proc))
file.close()