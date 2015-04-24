#!/usr/bin/python
'''
A simple network back-up script.
It was originally based on the http://habrahabr.ru/post/236483/ thread and comments

Usage:
  I use it with with crond to run daily. There are no command-line parameters to provide.
  Before using, configure the variables in the initial section.
  Then test if it even works. If it does, test if you can recover your files from the archive.

Procedure:
  1.  Copy Selected dir's (recursively), while preserving permissions to ./backup/
  1.a N.B.: a full backup is performed only on the 1st and the 15th day of month, on other days - just recently changed files are copied.
  2.  (optionally) mysqldump --all-databases
  3.  tar | 7z them with some password
  4.  (optionally) GPG encrypt the 7z arch
  5.  Upload to Dropbox using their API (you'll need to create your own app with them)
  6.  Clean up the mess, i.e. rm -r tempdir/*

TO DO: proper logging

Dependencies:
  linux - the script was intendend for backing up linux boxes, so mkdir, cp and tar should be present
  dropbox API SDK: pip install dropbox
  mysqldump for mysql backup
  7zip - I use the 7za tool
  unobstructed Internet access - I'm not sure this script will work from behind a proxy or a firewall
    (dropbox API makes tcp/443 (HTTPS) connections, probably DNS is needed as well)
  gpg - used for (optional) encryption

NOTICE&DISCLAIMER: 
  Understand that this is a very simple script and it was not meant for serious business. 
  Do not rely on it if you need to back up critical data.
  There is No support, No warranties, No responsibility whatsoever. Use at your own risk.

'''

# TO DO: this script ABSOLUTELY needs a better logging and a proc for sending me a message
import os
import sys
import time
import string
from os.path import getsize, exists

#Basic settings:
#Backup name:
BACKUP_NAME = "server"
#List the directories to backup here:
dirstobackup = ("/var/www/", "/home/", "/etc/", "/usr/local/sbin/", "/usr/local/bin/")

#base directory to store temp files:
tempdir='/tmp/backup'

# CHANGE this to some strong password, and the more characters, the better.
# 20 chars is the recommended minimum at the time of writing.
# consult with your security policy if you don't have one, follow some people you trust
# also, read https://en.wikipedia.org/wiki/Password_strength and exercise common sense
ARCHIVE_PASSWORD = 'MakeItAStrongOne!12345'
# WARNING: back your chosen password up, it is required to restore the data

#If MySQL database should be backed up
BACKUP_MYSQL = True 
# It is unwise to use the root user here!
'''
RTFM: https://dev.mysql.com/doc/refman/5.6/en/mysqldump.html
...requires at least the SELECT privilege for dumped tables, SHOW VIEW for dumped views, TRIGGER for dumped triggers, and LOCK TABLES if the --single-transaction option is not used.
'''
MYSQL_USER = 'user'
MYSQL_PASSWD = 'password'
# WARNING: the command used attempts to dump ALL databases to a text file

# Encrypt the archive with GPG public key before uploading?
GPG_ENCRYPTION = True
GPG_KEY_ID = 'YOUR-GPG-PUBLIC-KEY-ID' #public key must be present in GPG store
# WARNING: do not ever store the private key on the same server!!!
# WARNING: have your private and public (and possibly even revocation) keys stored somewhere safe
#          if GPG encryption is used, there is _enough_ probability that data won't be restored in
#          time if the key is lost. Therefore, without the matching private key there is no backup.


# Get your app key and secret from the Dropbox developer website https://www.dropbox.com/developers/apps
APP_KEY = 'your-dropbox-app-key'
APP_SECRET = 'your-dropbox-app-secret'
# Keep your keys & secrets secret!

# Optional additional WEBDAV upload (to Yandex.Disk in this example)
# I have not tested it, so it is present here merely for completeness
WEBDAV = False
WEBDAV_USER='USER'
WEBDAV_PASSWORD='PASSWORD'
WEBDAV_HOST='https://webdav.yandex.ru/'
# NOTE: same password recommendations apply.
'''
****************************************************************
***************Nothing to edit below this line******************
****************************************************************
'''
# I use this proc to catch external command error codes:
def syscmd(cmd):
 try:
  a=os.system(cmd)
 except Exception:
      pass
 if not a==0:
  print "ERROR code "+a+" while trying to run "+cmd 

# Include the Dropbox SDK libraries
import dropbox

def dropboxConnectionInit():
  oauth_token = ''
  DROPBOX_TOKEN_STORE = "dropbox-token.txt" # we need at least read rights on this file, RW is better
  if exists(DROPBOX_TOKEN_STORE):
   f = open(DROPBOX_TOKEN_STORE,'r') #whoever is in possession of this token is able to RW the app_dir
   if f:
    oauth_token = string.strip(f.readline())
    f.close()
    print "oauth token found:", oauth_token
  if oauth_token == '':
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
    # Authorize the application on dropbox site
    url = flow.start()
    print '1. Go to: ' + url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()
    # This will fail if the user didn't visit the above URL and hit 'Allow'
    # This will also fail if the user enters an invalid authorization code
    oauth_token = flow.finish(code)
    f = open(DROPBOX_TOKEN_STORE,"wb")
    f.write(oauth_token)
    f.close()
  client = dropbox.client.DropboxClient(oauth_token)
  print "Linked account:", client.account_info()[u'email']
  return client

def sync_dir(dir):
  rootdir = dir
  print "Syncing directory: ", rootdir
  startTime = backupDelay
  for root, subFolders, files in os.walk(rootdir):
    for file in files:
      fname = os.path.join(root,file)
      if os.path.getmtime(fname)>startTime:
        #copy files:
        syscmd("mkdir -p '"+tempdir+root+"'")
        syscmd("cp -p '"+fname+"' '"+tempdir+fname+"'")



def main():
  curDate = time.strftime("%Y%m%d", time.gmtime())
  curDay = time.strftime("%d", time.gmtime())
  backupDelay = time.time()-86400
  if ((curDay == "01") or (curDay == "15")):
    backupDelay = 0
  print "Date:", curDate
  if not exists(tempdir):
    syscmd("mkdir -p '"+tempdir+"'")
  for dir in dirstobackup:
    sync_dir(dir)
  if BACKUP_MYSQL:
    print "Making dump of MySQL databases..."
    syscmd("mysqldump --all-databases -u"+MYSQL_USER+" -p"+MYSQL_PASSWD+" -r "+tempdir+"/backup.sql")
  backupName = BACKUP_NAME+'_backup_'+curDate
  print "Creating archive file with name", backupName
  #TAR will try to preserve access rights:
  syscmd("tar -pcf "+tempdir+"/"+backupName+".tar "+tempdir+"/*")
  backupName = backupName+".tar"
  syscmd("7za a -p"+ARCHIVE_PASSWORD+" "+tempdir+"/"+backupName+".7z "+tempdir+"/"+backupName+" -y -mhe -mx=9 -t7z")
  backupName = backupName+".7z"
  cryptbackupName = backupName #safeguard if no PGP/GPG is used
  #never trust a simple password:
  if GPG_ENCRYPTION:
    print "Encrypting archive ", backupName
    cryptbackupName = 'crypted.'+backupName+'.pgp'
    syscmd("gpg --trust-model=always --yes -e -r 0x"+GPG_KEY_ID+" -o " +tempdir+"/"+ cryptbackupName + " " +tempdir+"/"+ backupName + "")
  client = dropboxConnectionInit()
  f = open(tempdir+"/"+cryptbackupName,'rb')
  if f:
    fsize = getsize(tempdir+"/"+cryptbackupName)
    uploader = client.get_chunked_uploader(f, fsize)
    print "Uploading file of", fsize, "bytes..."
    while uploader.offset < fsize:
      try:
        upload = uploader.upload_chunked()
        print "."
      except rest.ErrorResponse, e:
        # perform error handling and retry logic
        print "Error uploading file!"
    uploader.finish("/"+cryptbackupName)
    f.close()
    print "File uploaded to Dropbox successfully."
  #Just in case:
  if WEBDAV:
    syscmd("curl --user "+WEBDAV_USER+":"+WEBDAV_PASSWORD+" -T "+tempdir+"/"+cryptbackupName+" "+WEBDAV_HOST)
  print "Removing temp files..."
  syscmd("rm -r "+tempdir+"/*")
  print "Backup complete"


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

#EOF