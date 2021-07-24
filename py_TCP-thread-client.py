import socket
import threading

# set target info
ip = "127.0.0.1"
port = 4444

def handle_cli_input(cli):
	# continuously get requests and send
	while True:
		request = input()
		request += "\n"
		
		# send on condition
		if len(request):
			try:
				print("\n")
				print("[>] Sending ",len(request)," bytes of data")
				cli.send(str.encode(request))
			except Exception as e:
				# terminate
				print("[-] Sending failor: ",str(e))
				cli.close()
				exit()

def main():
	# create socket - TCP/IPv4
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# attempt connection
	try:
		client.connect((ip, port))
		print("[+] Connected to %s/%d" % (ip, port))
		
	except Exception as e:
		print("[-] Connection failor: ",str(e))
		exit()
		
	# communicate
	
	# start a thread for input
	get_input = threading.Thread(target=handle_cli_input, args=(client,))
	get_input.start()
	
	while True:		
		# receive and print data
		try:
			response = client.recv(1024)
			print("[<] Received ",len(response[:].decode("utf-8"))," bytes of data")
			print("\nRE ~ ",response[:].decode("utf-8"))
			
		except Exception as e:
			# terminate
			print("[-] Receipt failor: ",str(e))
			client.close()
			exit()
		
main()
		


