import pickle
import subprocess
import sys

if __name__ == "__main__":
	blacklist = []
	if (str(sys.argv[1]) == "-f"):
		with open("blacklist.txt", "wb") as fp:
			pickle.dump(blacklist, fp)
			subprocess.run(['iptables', '-F'])
			print(blacklist)
			fp.close()
	elif (str(sys.argv[1]) == "-p"):
		with open("blacklist.txt", "rb") as fp:
			blacklist = pickle.load(fp)
			print(blacklist)
			fp.close()
	elif (str(sys.argv[1]) == "-h"):
		print('-f	flushes iptables and blacklist\n-p		prints the blacklist')