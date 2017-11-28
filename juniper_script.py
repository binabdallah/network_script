
import paramiko
import time
import re
import sys

def open_ssh_conn(ip):
    try:
        
        user_file=raw_input("enter valid users file name : ")
        conf_file=raw_input("enter valid command file name : ")
        selecte_user=open(user_file,'r')
        selecte_user.seek(0)
        username=selecte_user.readlines()[0].split(',')[0]
        selected_user.seek(0)
        passwordselecte_user.readlines()[0].split(',')[1].rstrip("\n")
        session=paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip,username=username,password=password)
        connection = session.invoke_shell()
        connection.send("terminal length 0\n")
        time.sleep(1)
        connection.send('\n')
        connection.send("conf terminal")
        select_cmd_file=open(conf_file,"r")
        select_cmd_file.seek(0)
        for each_line in select_cmd_file.readline():
            connection.send(each_line + '\n')
            time.sleep(2)
            selecte_user.close()
            select_cmd_file.close()
            router_output=connection.recv(65535)
        connection.close()    
    except IOError
        print 'error'
        
