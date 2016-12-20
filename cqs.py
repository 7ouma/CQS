#!/usr/bin/env python2.7
# -*- coding: cp1252 -*-
import os
import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
import qrcode
import socket
import urllib
from time import sleep
def files (url):
    if not os.path.isdir(os.getcwd()+"/cia"):
        os.mkdir("cia")
    i = 0
    print "########## CIAs Found ##########"
    for file in os.listdir(os.getcwd()+"/cia"):
    	if file.endswith(".cia".lower()):     
            print file
            img = qrcode.make(url+urllib.quote(file))
            img.save("cia/"+file+".png")
            i+=1
    if i == 0:
        print "No .cia files were found. Make sure to put your cia files inside /cia"
    print "################################"
    if i == 0:       
        sleep(5)
        return False
    return True
def server(HandlerClass=SimpleHTTPRequestHandler,
         ServerClass=BaseHTTPServer.HTTPServer):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 0))
    IP = s.getsockname()[0]
    s.close() 
    protocol = "HTTP/1.0"
    port = 8080
    server_address = (IP, port)
    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    if files("http://"+str(IP)+":"+str(port)+"/cia/"): 
        print "\nServing HTTP on", sa[0], "port", sa[1], "..."  
        httpd.serve_forever()

if __name__ == "__main__":
	print "https://github.com/7ouma/CQS"
	server()
