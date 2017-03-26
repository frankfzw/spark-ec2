#!/usr/bin/env python

import subprocess
import time
from os.path import expanduser

cmd = 'cat /proc/stat'

prev_idle = 0
prev_nonidle = 0
init = False

home = expanduser('~')

f = open('{}/cpu.txt'.format(home), 'w+')
f.close()

while True:
	result = subprocess.check_output(cmd, shell=True)
	cpu_line = result.split('\n')[0]
	args = cpu_line.split()
	user = int(args[1])
	nice = int(args[2])
	system = int(args[3])
	idle = int(args[4])
	iowait = int(args[5])
	irq = int(args[6])
	softirq = int(args[7])
	steal = int(args[8])
	guest = int(args[9])
	guest_nice = int(args[10])
	if not init:
		prev_idle = idle + iowait
		prev_nonidle = user + nice + system + irq + softirq + steal
		init = True
	else:
		now_idle = idle + iowait
		now_nonidle = user + nice + system + irq + softirq + steal
		prev_total = prev_idle + prev_nonidle
		totald = now_idle + now_nonidle - prev_total
		idled = now_idle - prev_idle
		cpu_util = float(totald - idled)/float(totald)
		prev_idle = now_idle
		prev_nonidle = now_nonidle
		log_str = '{} {}\n'.format(time.ctime(), cpu_util)
		with open('{}/cpu.txt'.format(home), 'a') as f:
			f.write(log_str)
	time.sleep(0.5)

