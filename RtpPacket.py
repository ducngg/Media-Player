import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:	
	header = bytearray(HEADER_SIZE)
	
	def __init__(self):
		pass
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		#print('RtpPacket: def encode')
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields
		
		# header[0] 8 bit
		header[0] = version << 6 | padding << 5 | extension << 4 | cc
			# version	xx.. .... 
			# padding	..x. .... 
			# extension	...x ....
			# con. cnt. .... xxxx
   
		# header[1] 8 bit
		header[1] = marker << 7 | pt
			# marker	x... .... 
			# p. type 	.xxx xxxx 
   
		# header[2] 8 bit, header[3] 8 bit
		header[2] = seqnum >> 8
		header[3] = seqnum & 0xFF
			# header2	xxxx xxxx  (seqnum 16 bit: 'xxxx xxxx yyyy yyyy')
			# header3   yyyy yyyy
   
   		# header[4] 8 bit, header[5] 8 bit, header[6] 8 bit, header[7] 8 bit
		header[4] = (timestamp >> 24) & 0xFF
		header[5] = (timestamp >> 16) & 0xFF
		header[6] = (timestamp >> 8 ) & 0xFF
		header[7] = (timestamp) 	  & 0xFF
			# header4	xxxx xxxx  (timestamp 32 bit: 'xxxx xxxx yyyy yyyy zzzz zzzz tttt tttt')
			# header5   yyyy yyyy
   			# header6	zzzz zzzz  
			# header7   tttt tttt
  
		# header[8] 8 bit, header[9] 8 bit, header[10] 8 bit, header[11] 8 bit
		header[8]  = (ssrc >> 24) & 0xFF
		header[9]  = (ssrc >> 16) & 0xFF
		header[10] = (ssrc >> 8 ) & 0xFF
		header[11] = (ssrc)		  & 0xFF
			# header8	xxxx xxxx  (ssrc 32 bit: 'xxxx xxxx yyyy yyyy zzzz zzzz tttt tttt')
			# header9   yyyy yyyy
   			# header10	zzzz zzzz  
			# header11  tttt tttt
  
		self.header = header
		self.payload = payload

	def decode(self, byteStream):
		# print('RtpPacket::decode()')
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		# print('RtpPacket::version()')
		"""Return RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		# print('RtpPacket::seqNum()')
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		# print('RtpPacket::timestamp()')
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		# print('RtpPacket::payloadType()')
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		# print('RtpPacket::getPayload()')
		"""Return payload."""
		return self.payload
		
	def getPacket(self):
		# print('RtpPacket::getPacket()')
		"""Return RTP packet."""
		return self.header + self.payload