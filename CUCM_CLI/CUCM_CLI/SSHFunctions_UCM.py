#!/usr/bin/python
# PSFL license
# Importing SSHClientInteraction from paramiko
import paramiko
from paramiko_expect import SSHClientInteraction
import paramiko_expect
import sys
from datetime import datetime
# Specify connection info for each node in square brackets: ["IP ADDRESS", "USERNAME", "PASSWORD"]

# Define function which is responsible for opening SSH connection and running specified commands
def ChangeUsername(ip, username, password, command, Username):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(ip, username=username, password=password)
    # "display=True" is just to show you what script does in real time. While in production you can set it to False
    interact = SSHClientInteraction(sshsession, timeout=600, display=True)
    # program will wait till session is established and CUCM returns admin prompt
    interact.expect('admin:')
    output = interact.current_output_clean  # program saves output of show status command to the "output" variable
    interact.send(command)
    interact.last_match == '.*administrator.*'
    interact.send(Username)
    interact.expect('admin:')
    output = interact.current_output_clean  # program saves output of show status command to the "output" variable
    with open("Logs/ChangeAdminName.txt", 'a') as outfile:
        outfile.write(f"{output} {username} -- Administrator Name Changed to {Username} {datetime.now()}")
        outfile.close()
    sshsession.close()


def ChangeAppPassword_interact(ip, username, password, command, appPassword):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(ip, username=username, password=password)
    # "display=True" is just to show you what script does in real time. While in production you can set it to False
    interact = SSHClientInteraction(sshsession, timeout=600, display=True)
    # program will wait till session is established and CUCM returns admin prompt
    interact.expect('admin:')
    interact.send(command)
    interact.expect('.*password:.*')
    interact.send(appPassword)
    interact.expect('.*Password:.*')
    interact.send(appPassword)
    interact.expect('admin:')
    output = interact.current_output # program saves output of show status command to the "output" variable
    with open("Logs/ChangeAdminPw.txt", 'a') as outfile:
        outfile.write("{0} {1} -- Password Initiated changed to {2} {3}".format(output, username, appPassword, datetime.now()))
        outfile.close()
    sshsession.close()
    


def ShowCommands(ip, username, password, command):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(ip, username=username, password=password)
    # "display=True" is just to show you what script does in real time. While in production you can set it to False
    interact = SSHClientInteraction(sshsession, timeout=600, display=True)
    # program will wait till session is established and CUCM returns admin prompt
    interact.expect('admin:')
    interact.send(command)
    interact.expect('admin:')
    output = interact.current_output  # program saves output of show status command to the "output" variable
    with open("Logs/ShowCommand.txt", 'a') as outfile:
        outfile.write(output)
        outfile.close()
    sshsession.close()
   
def ChangePlatformPw(ip,username,password,NewPlatPw,command):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(ip, username=username, password=password)
    # "display=True" is just to show you what script does in real time. While in production you can set it to False
    interact = SSHClientInteraction(sshsession, timeout=600, display=True)
    # program will wait till session is established and CUCM returns admin prompt
    # "display=True" is just to show you what script does in real time. While in production you can set it to False
    interact = SSHClientInteraction(sshsession, timeout=600, display=True)
    # program will wait till session is established and CUCM returns admin prompt
    interact.expect('admin:')
    interact.send(command)
    interact.expect('.*password:.*')
    interact.send(password)
    interact.expect('.*password:.*')
    interact.send(NewPlatPw)
    interact.expect('.*password.*')
    interact.send(NewPlatPw)
    interact.expect('admin:')
    output = interact.current_output  # program saves output of show status command to the "output" variable
    with open("Logs/ChangeAppPw.txt", 'a') as outfile:
        outfile.write(output)
        outfile.write("{0} {1} -- Password Initiated changed to {2} {3}".format(ip, username, NewPlatPw,datetime.now()))
        outfile.close()
    sshsession.close()
