import subprocess
import pickle

def count_occurrances():
	subprocess.run(['chmod', '+x', './log.sh'])
	output = subprocess.check_output('./log.sh').decode('utf-8').split()
	for i in range(len(output)):
		if i % 2 == 0:
			print("addr:", output[i + 1], "tries:", output[i])
			if (int(output[i]) >= 20):
				with open("whitelist.txt", "rb") as fp:
					whitelist = pickle.load(fp)
					if (not output[i + 1] in whitelist):
						subprocess.run(['iptables', '-A', 'INPUT', '-s', output[i + 1], '-j', 'DROP'])
						print("Access restricted to", output[i + 1])
					else:
						print("forgot something?")