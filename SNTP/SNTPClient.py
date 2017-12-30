import socket
import struct
import sys
import time
import datetime

NTP_SERVER = "1.ca.pool.ntp.org"
s = "01/01/1970"
TIME1970 = time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())


def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = str.encode('\x1b' + 47 * '\0')
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)
    if data:
        print('Response received from:', address)
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))


if __name__ == '__main__':
    sntp_client()
