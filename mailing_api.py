import requests

def send_simple_message(file_content):
    return requests.post(
        "https://api.mailgun.net/v3/[your mail gun url]/messages",
        auth=("api", "[your api key]"),
        data={"from": "[sender] <postmaster@[your mail gun url]>",
              "to": "[receiver's name] <[receiver's email address]>",
              "subject": "[subject]",
              "text":  file_content
              })

def send_LOG():
    return requests.post(
        "https://api.mailgun.net/v3/[your mail gun url]/messages",
        auth=("api", "[your api key]"),
        files=[("attachment", open("Process_list.txt"))],
        data={"from": "PSManagerFromLaptop_1 <postmaster@[your mail gun url]>",
              "to": "name <[receiver's name]>",
              "subject": "Hello name, Here is captured Process Logfile",
              "text": "CAPTURED PROCESS LOGFILE you should view on google docs"
              })
