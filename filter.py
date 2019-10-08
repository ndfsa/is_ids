from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess
import time

def on_created(event):
	print("Log file created")

def on_deleted(event):
	print("Log file deleted")
    
def on_modified(event):
	print("Log file modified")
    
def on_moved(event):
	print("Log file moved")

def start():
	patterns = "auth.log"
	ignore_patterns = ""
	ignore_directories = False
	case_sensitive = True
	event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

	event_handler.on_created = on_created
	event_handler.on_deleted = on_deleted
	event_handler.on_modified = on_modified
	event_handler.on_moved = on_moved

	path = "/var/log/auth.log"
	go_recursively = True
	observer = Observer()
	observer.schedule(event_handler, path, recursive=go_recursively)

	subprocess.run('iptables -N LOGGING; iptables -A INPUT -j LOGGING; iptables -A LOGGING -m limit --limit 2/min -j LOG --log-prefix "IPTables-Dropped: " --log-level 4', shell=True)

	observer.start()
	try:
		while True:
			time.sleep(10)
	except KeyboardInterrupt:
		observer.stop()
		observer.join()