# Media-Player
A real video server and client that communicate using the Real-Time Streaming Protocol (RTSP) and send data using the Real-Time Transfer Protocol (RTP).
User manual:

To use, we need to create 2 terminals. One present for the server and one for the client.
Server requires a port number:
>> python3 Server.py 8000

Client requires the IP of the Server, port number, a RTP port and the file:
>> python3 ClientLauncher.py 192.168.1.17 8000 80 movie.Mjpeg

After running the above setup, here is the pop-up window.
<img width="553" alt="image" src="https://github.com/ducngg/Media-Player/assets/89516843/12b3302d-b5ef-4e52-9a3d-7dcb8c64cf0a">
There are buttons for play, pause, forward, backward, stop, and describe, where the describe button shows information about the movie played.
