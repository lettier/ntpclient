'''

(C) 2014 David Lettier.

http://www.lettier.com/

NTP client.

'''

from socket import AF_INET, SOCK_DGRAM # For setting up the UDP packet.
import sys
import socket
import struct, time # To unpack the packet sent back and to convert the seconds to a string.

host = "pool.ntp.org"; # The server.
port = 123; # Port.
read_buffer = 1024; # The size of the buffer to read in the received UDP packet.
address = ( host, port ); # Tuple needed by sendto.
data = '\x1b' + 47 * '\0'; # Hex message to send to the server.

epoch = 2208988800L; # Time in seconds since Jan, 1970 for UNIX epoch.

client = socket.socket( AF_INET, SOCK_DGRAM ); # Internet, UDP

client.sendto( data, address ); # Aend the UDP packet to the server on the port.

data, address = client.recvfrom( read_buffer ); # Get the response and put it in data and put the send socket address into address.

t = struct.unpack( "!12I", data )[ 10 ]; # Unpack the binary data and get the seconds out.

t -= epoch; # Calculate seconds since the epoch.

print "Time = %s" % time.ctime( t ); # Print the seconds as a formatted string.
