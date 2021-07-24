import socket
import threading

def handle_svr_reciept(cli_connection):
	while True:
		# receive data
		try:
			data = cli_connection.recv(4096)
		except Exception as e:
			print("[-] Reciept failor: ",str(e))
			cli_connection.close()
			exit(-1)
			
		print("\nRE ~ ",data[:].decode("utf-8"),"\n")
		
			
def handle_svr_input(cli_connection):
	# continuousky get input and send
	while True:
		response = input()
		response += "\n"
		
		try:
			print("\n")
			print("[>] Sending ",len(response)," bytes")
			cli_connection.send(str.encode(response))
			
		except Exception as e:
			# terminate
			print("[-] Sending failor: ",str(e))
			cli_connection.close()
			exit()
	
	
def main():
	# set svr info
	ip = "127.0.0.1"
	port = 4444
	
	# create socket - TCP/IPv4
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# attempt to bind and listen
	try:
		print("[+] Binding and listening on %s/%d" % (ip, port))
		server.bind((ip, port))
		server.listen(1)
		
	except Exception as e:
		print("[-] Bind and listen failor: ",str(e))
		exit()
		
	# accept incoming connection and handle
	while True:
		cli_con, cli_info = server.accept()
		print("[+] Connection from %s/%d" % (cli_info[0], cli_info[1]))
		
		# create thread for handleing input
		get_input = threading.Thread(target=handle_svr_reciept, args=(cli_con,))
		get_input.start()
		
		while True:		
			# handle receipt of input and display
			try:
				#data = cli_con.recv(1024)
				#print("[<] Received ",len(data[:].decode("utf-8"))," bytes\n")
				#print("~ ",data[:].decode("utf-8"))
				req = input()
				req += "\n"
				
				# send
				cli_con.send(str.encode(req))
			
			except Exception as e:
				# terminate
				print("[-] Send failor: ",str(e))
				cli_con.close()
				exit()
			
main()