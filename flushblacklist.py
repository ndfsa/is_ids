import pickle

if __name__ == "__main__":
	blacklist = []
	
	with open("blacklist.txt", "wb") as fp:
		pickle.dump(blacklist, fp)
		print(blacklist)
		fp.close()
