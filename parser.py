import datetime
import re
import subprocess

def count_occurrances(lines):
	command = '''cat /var/log/auth.log | grep "Failed pass" | awk {print $11} | sort -nr'''
	process = subprocess.run([command])
	for i in process.stdout:
		print(i)

