import pysftp
from datetime import date
import shutil
import os
from zipfile import ZipFile


#Connection details
myHostname = <"ip address">
myUsername = <"username">
myPassword = <"password">

#initiate connection to the sftp server
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
    #print below when connection is succesful
    print ("Connection succesfully stablished ... ")

    # change directoy to the root directoy of the remote directory
    sftp.cwd('/')

    # Output the list of the content of the current remote directory
    directory_structure = sftp.listdir_attr()
    for attr in directory_structure:
        print (attr.filename, attr)


    #below is to constract the name of the zip file to be downloaded as in sace below it had dates appended to the file.
    today = date.today()
    name = str(date(year=today.year, month=today.month, day=today.day))
    download = 'World__' + name + '.zip'
    #This downloads the file
    sftp.get('/' + download,
             download)



print(download)


print('Downloading zip file')

print('lets unzip.....................................')
# specifying the zip file name after it has been unzipped
file_name = download
inFile = 'World__' + name + '.xml'
#This part below unlocks the zipfile with the password and unzips then uses above code to constract
#the XML file name afte unzip the closes the unzipping process.
myzip = ZipFile(file_name, 'r')
myfile = myzip.extract(inFile, pwd=b<'zipfile_password'>)
print('Done unzipping..............')

myzip.close()


#This last part renames the file to the desired name and saves it in a desired path to be consumed.
files = [inFile]
for f in files:
    shutil.move(f, 'D:\World\peace\Extracted')
