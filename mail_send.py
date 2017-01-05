from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from os.path import basename
import smtplib
COMMASPACE = ', '
msg = MIMEMultipart()
msg['Subject'] = 'Our family reunion'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = "LOGMANAGER <postmaster@mg.ladmail.com>"
msg['To'] = "LAD <hth225@gmail.com>"
msg.preamble = 'New log.png file was arrived'

# Assume we know that the image files are all in PNG format
for file in file.png:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
    with open(file, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)

# smtp = smtplib.SMTP_SSL(host='smart.whoismail.net', port=587)
smtp = smtplib.SMTP(host='smtp.mailgun.org', port=587)
smtp.login("postmaster@mg.ladmail.com", "28ef0be551dbbc27696ce4d2f6ca20c1 ")