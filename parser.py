import datetime
import re
import subprocess

def count_occurrances():
	output = subprocess.check_output('bash log.sh')
	print(output)
