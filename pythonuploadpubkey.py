#This will upload your public ssh key file into /home/name/.ssh/authrorized_key ahd set chmod 645 to authorized_keys
#made by gh0st
#irc.twistednet.org #twisted

import os
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#input server information below
ssh.connect('127.0.0.1', username="root", password="password")
sftp = ssh.open_sftp()
#change below to the location of your rsa.pub file
localpath = 'id_rsa.pub'
#change below to the dir you wish your rsa.pub to be uploaded to
remotepath = '/root/.ssh/authorized_keys'
newdir = '.ssh'
keyfile = "authrorized_keys"
mode = '645'
sftp.mkdir(newdir)
sftp.put(localpath, remotepath)
sftp.chmod(remotepath, 0o645)
sftp.close()
ssh.close()
print('all done')