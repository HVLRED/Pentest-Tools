from scapy.all import *
import signal
import sys
from datetime import datetime, timedelta

print()
print("Sniffing all ARP connections, press Ctrl+C to end")
do_save_results = False
try:
	filename_base = sys.argv[1]

	filename_arp_add = filename_base + "_arp_add.sh"
	filename_arp_del = filename_base + "_arp_del.sh"
	filename_raw     = filename_base + "_raw.txt"
	do_save_results = True
	print("Will save final results and scripts at", filename_arp_add, filename_arp_del, filename_raw)
except:
	print("No filename provided, will not save results")

arpdict = dict()

def prn2(packet):
	if packet.haslayer(ARP):
		print(packet.psrc, " is at ", packet.hwsrc)
		
		try:
			if (packet.hwsrc != arpdict[packet.psrc]):
				print("MAC Address changed for IP", packet.psrc, "from", arpdict[packet.psrc], "to", packet.hwsrc, "at", datetime.now())
				print("Most recent version will be saved!")
		except:
			pass
		arpdict[packet.psrc] = packet.hwsrc 


def save_results(timestop,duration):
	

	
	arp_add_file = open(filename_arp_add, "w")
	arp_del_file = open(filename_arp_del, "w")
	raw_results_file = open(filename_raw, "w")
	
	arp_add_file.write("#!/bin/bash\n")
	arp_del_file.write("#!/bin/bash\n")
	
	raw_results_file.write(str(filename_raw+"\n" ))
	raw_results_file.write(str("ARP learning results between "+ str(timestart) + " and "+ str(timestop)+"\n" ))
	raw_results_file.write(str("Duration: " + str(duration)+"\n" ))
	
	for pair in arpdict.items():
		arp_add_file.write(str("arp -s " + str(pair[0]) + " " + str(pair[1])+"\n" ))
		arp_del_file.write(str("arp -d " + str(pair[0])+"\n" ))
		raw_results_file.write(str(str(pair[0]) + " has MAC address: " + str(pair[1])+"\n" ))
		
	arp_add_file.close()
	arp_del_file.close()
	raw_results_file.close()
	print("Saved final results and scripts at", filename_arp_add, filename_arp_del, filename_raw)	
		
def signal_handler(sig, frame):
	print()
	timestop = datetime.now()
	duration = timestop - timestart
	print("Sniffing stopped at ",timestop)
	print("Duration: ", duration)
	if do_save_results:
		save_results(timestop, duration)
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
timestart = datetime.now()
print()
print("Sniffing started at", timestart)
sniff(store=False, prn=prn2)





