import datetime
import re
import subprocess

def count_occurrances():
	subprocess.run(['chmod', '+x', './log.sh'])
	output = subprocess.check_output('./log.sh').encode().split()
	print("addr:", output[1], "tries:", output[0])
