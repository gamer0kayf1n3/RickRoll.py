from playsound import playsound

import os
print('importing file manager:')
def delf():
    os.remove('aud.mp3')
    os.remove('file.zip')
    print('ended')
import atexit
atexit.register(delf)
import base64 as b64
print('importing decryptor:')
from zipfile import ZipFile
import shutil
import time
print('0% done')

#let it work its magic
nope_message = 'dGhpc2lzZ2FtZXIwa2F5ZjFuM2FuZG1vbmlrYQ=='
print('20% done')

bruh = nope_message.encode('ascii')

print('60% done')
message_bytes = b64.b64decode(bruh)
print('80% done')
message = message_bytes.decode('ascii')
print('decryption done')

#set name to..
shutil.copy2('files.uknwn', 'file.zip')
print('copied')

# specifying the zip file name
file_name = "file.zip"
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    #zip.printdir()
    # extracting all the files
    zip.setpassword(bytes(message, 'utf-8'))

    zip.extractall()
    print('extracted')


#get them rickroll'd
playsound('aud.mp3')

#delete them afterwards ofc
delf()
time.sleep(3)
