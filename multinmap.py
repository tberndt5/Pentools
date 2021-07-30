import os
import time
import sys
import multiprocessing

# Define function for thread
def nmap_scan(IP):
	try:
		os.system("nmap -sV -sC -A %s -oG %s.txt" % (IP,IP))
	except:
		print("[ERROR] Could not scan on %s" % (IP))


if __name__ == "__main__":
	if sys.argv == 1:
		print("[ERROR] Not enough arguements..")
		print("Run the script with IP addresses as additional arguements")

	else:
		jobs = []
		for ip in sys.argv[1:]:
			process = multiprocessing.Process(target=nmap_scan(ip))
			jobs.append(process)

		for j in jobs:
			j.start()

		for j in jobs:
			j.join()

		print("Nmap scans complete!")
