#!/usr/bin/bash
tail -n 500 /var/log/auth.log | grep "Failed pass" | awk '{print $11}' | uniq -c | sort -nr | head -n 5