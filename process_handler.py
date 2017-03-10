import subprocess

def processlist_sort():
    file = open("Process_list.txt", "r")
    sortedlist = file.read()
    sortedlist.replace("\r\r\n'b'", "\t")

def parse_process_list():
    cmd = 'tasklist /v'
    proc = subprocess.getoutput(cmd).split("\n")
    file = open("Process_list.txt", "w+")
    file.write(str(proc))
    file.close()
