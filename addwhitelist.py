import pickle
import sys

if __name__ == "__main__":
	whitelist = []
	if (str(sys.argv[1]) == "-f"):
		with open("whitelist.txt", "wb") as fp:
			pickle.dump(whitelist, fp)
			print(whitelist)
			fp.close
	elif (str(sys.argv[1]) == "-A"):
		with open("whitelist.txt", "rb") as fp:
			whitelist = pickle.load(fp)
			fp.close()
		ip = str(sys.argv[2])
		whitelist.append(ip)
		with open("whitelist.txt", "wb") as fp:
			pickle.dump(whitelist, fp)
			print(whitelist)
			fp.close
	elif (str(sys.argv[1]) == "-p"):
		with open("whitelist.txt", "rb") as fp:
			whitelist = pickle.load(fp)
			print(whitelist)
			fp.close()
	elif (str(sys.argv[1]) == "-h"):
		print("-f		flush whitelist\n -A	append an ip to whitelist\n -p		print whitelist")
	else:
		print("Invalid command, try -h for help")
