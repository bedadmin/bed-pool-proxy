#!/usr/bin/env python

import socket
import json
import sys
import argparse
import time

start = time.time()

parser = argparse.ArgumentParser(description='Add a litecoind server to the Stratum instance.')
parser.add_argument('--password', dest='password', type=str, help='use admin password from Stratum server config')
parser.add_argument('--host', dest='host', type=str, default='localhost', help='hostname of Stratum mining instance')
parser.add_argument('--port', dest='port', type=int, default=3333, help='port of Stratum mining instance')
parser.add_argument('--diff', dest='diff', type=int, default=10000, help='pool difficulty')

args = parser.parse_args()

if args.password == None:
	parser.print_help()
	sys.exit()
	
message = {'id': 1, 'method': 'mining.set_difficulty', 'params': [args.password, args.diff]}

print('Set pool difficulty to %s' %(args.diff))
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.host, args.port))
    s.sendall(json.dumps(message)+"\n")
    data = s.recv(16000)
    s.close()
except IOError:
    print "updatediff: Cannot connect to the pool"
    sys.exit()

print(data.strip())
