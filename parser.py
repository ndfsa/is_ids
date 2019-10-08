import datetime
import re
import subprocess

def count_occurrances():
	command = ['tail -n 50 /var/log/auth.log', 'grep "Failed pass"', 'awk {print $11}', 'sort -nr']
	process = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
	for i in process.stdout:
		out = i.split()
		print("Host:", out[1], "tries:", out[0])

