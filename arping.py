import sys
from datetime import datetime
from scapy.all import *

try:
    interface = input('Set interface: \n')
    ips = input('Ip range or Network: \n')
except KeyboardInterrupt:
    print('User Aborted')
    sys.exit()

print('Scanning ...')
start_time = datetime.now()
conf.verb = 0
ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst = ips), timeout = 2, iface = interface, inter = 0)
print('\n\tMAC\t\tIP')

for snd.rcv in ans:
    print(rcv.sprint('%Ether.src% - %ARP.psrc%'))
stop_time = datetime.now()
total_time = stop_time - start_time
print('Scan Completed\n')
print('Scan Duration: %s' %(total_time))
