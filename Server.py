import sys, socket
from ServerWorker import ServerWorker

class Server:
	
	def main(self):
		try:
			SERVER_PORT = int(sys.argv[1])
		except:
			print("[Usage: Server.py Server_port]\n")
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# Create IPv4 TCP socket
		rtspSocket.bind(('', SERVER_PORT)) 								# binding SERVER_PORT for socket
		rtspSocket.listen(5) 											# Maximum connections

		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			clientInfo['rtspSocket'] = rtspSocket.accept()
			ServerWorker(clientInfo).run()

if __name__ == "__main__":
	(Server()).main()