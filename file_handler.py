import pyscreenshot as ImageGrab
import datetime

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
