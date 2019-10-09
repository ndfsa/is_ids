import pickle
import subprocess

if __name__ == "__main__":
	blacklist = []
	
	with open("blacklist.txt", "wb") as fp:
		pickle.dump(blacklist, fp)
		subprocess.run(['iptables', '-F'])
		print(blacklist)
		fp.close()
