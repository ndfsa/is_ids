from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

patterns = "*"
ignore_patterns = ""
ignore_directories = False
case_sensitive = True
event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    print("Log file created")

def on_deleted(event):
	print("Log file deleted")
    
def on_modified(event):
	print("Log file modified")
    
def on_moved(event):
    print("Log file moved")

event_handler.on_created = on_created
event_handler.on_deleted = on_deleted
event_handler.on_modified = on_modified
event_handler.on_moved = on_moved