#!/usr/bin/python

import os
import serial
import SocketServer

for n in range (0, 10):
    try:
        ser = serial.Serial("/dev/tty.usbmodem1411", 9600)
        print "Connected /dev/cu.usbmodem1411"
        break
    except:
        print "Could not connect /dev/cu.usbmodem1411"

if not 'ser' in globals():
    os._exit(-2)

class MyUDPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print data
        try:
            ser.write(data)
            ser.write('\n')
        except:
            os._exit(-1)

if __name__ == "__main__":
    HOST, PORT = "", 9999
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
