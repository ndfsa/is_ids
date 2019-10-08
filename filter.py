from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess
import time
import parser

def on_created(event):
	print("Log file created")

def on_deleted(event):
	print("LOG FILE DELETED, SOMETHING'S WRONG")
    
def on_modified(event):
	print("Log file modified")
	parser.count_occurrances()
    
def on_moved(event):
	print("LOG FILE MOVED, WTF")

def start():
	patterns = "*/auth.log"
	ignore_patterns = ""
	ignore_directories = False
	case_sensitive = True
	event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

	event_handler.on_created = on_created
	event_handler.on_deleted = on_deleted
	event_handler.on_modified = on_modified
	event_handler.on_moved = on_moved

	path = "/var/log/"
	go_recursively = True
	observer = Observer()
	observer.schedule(event_handler, path, recursive=go_recursively)

	observer.start()
	try:
		while True:
			time.sleep(500)
	except KeyboardInterrupt:
		observer.stop()
		observer.join()