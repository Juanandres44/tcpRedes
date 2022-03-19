import ftplib

ftp = ftplib.FTP('ftp.dlptest.com')

ftp.login('user', '12345')


ftp.retrlines('LIST')


ftp.retrbinary('RETR FTP.txt', open('archivodescargado.txt', 'wb').write)

import os

os.listdir()
