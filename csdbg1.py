import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("--ip", help='enter the ip here')
parser.add_argument("--target", help='enter the process name here')
parser.add_argument("--pid", help='enter process id here')
parser.add_argument('-v', "--verbose", action='store_true', help='verbosely prints the hex encoded contents of the packet')

args = parser.parse_args()

if args.ip is None:
  print("You must enter an IP")
else:
  try:
    socket.inet_aton(args.ip)
  except socket.error:
    print('invalid ip')

if args.target is not None and args.pid is not None:
  print('you must only enter a process name or a pid, NOT BOTH')
elif args.pid is not None:
 print(args.ip,args.pid)
 session_start = bytes.fromhex('00')
 hexpid = args.pid.encode("utf-8").hex()
else:
  print(args.ip, args.target)
  session_start = bytes.fromhex('01')
  hextarget = args.target.encode("utf-8").hex()
#print(session_start)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((args.ip, 1337))
magic_bytes = bytes.fromhex('6373db67')
message_type = bytes.fromhex('00')
if session_start is bytes.fromhex('00'):
  #print('pid')
  data = bytes.fromhex(hexpid)
  packet = magic_bytes+message_type+session_start+data
elif session_start is bytes.fromhex('01'):
  #print('target')
  datastring = bytes.fromhex('07')
  data = bytes.fromhex(hextarget)
  packet = magic_bytes+message_type+session_start+datastring+data


if args.verbose is not None:
  print(packet)

try:
    s.sendall(packet)
except socket.error:
  print("failure")
  exit()
print('success')

