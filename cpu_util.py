#!/usr/bin/env python

import subprocess
import time
from os.path import expanduser

cpu = 'cat /proc/stat'
disk = 'cat /proc/diskstats'
network = 'cat /proc/net/dev'
disk_name = 'xvda1'
if_name = 'eth0'

prev_idle = 0
prev_nonidle = 0
init = False

prev_scetor_r = 0;
prev_sector_w = 0;

prev_rx = 0;
prev_tx = 0;

home = expanduser('~')

f = open('{0}/cpu.txt'.format(home), 'w+')
f.write('timestamp usage\n')
f.close()
f = open('{0}/disk.txt'.format(home), 'w+')
f.write('timestamp read(KB/s) write(KB/s)\n')
f.close()
f = open('{0}/net.txt'.format(home), 'w+')
f.write('timestamp rx(KB/s) tx(KB/s)\n')
f.close()

while True:
	ts = long(round(time.time() * 1000))
	# cpu
	result = subprocess.Popen(cpu.split(), stdout=subprocess.PIPE).communicate()[0]
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
	else:
		now_idle = idle + iowait
		now_nonidle = user + nice + system + irq + softirq + steal
		prev_total = prev_idle + prev_nonidle
		totald = now_idle + now_nonidle - prev_total
		idled = now_idle - prev_idle
		cpu_util = float(totald - idled)/float(totald)
		prev_idle = now_idle
		prev_nonidle = now_nonidle
		log_str = '{0} {1}\n'.format(ts, cpu_util)
		with open('{0}/cpu.txt'.format(home), 'a') as f:
			f.write(log_str)
			f.close()
	# disk 
	result = subprocess.Popen(disk.split(), stdout=subprocess.PIPE).communicate()[0]
	lines = result.split('\n')
	disk_line = ''
	for l in lines:
		if disk_name in l:
			disk_line = l
			break
	args = disk_line.split()
	if not init:
		prev_scetor_r = int(args[5])
		prev_sector_w = int(args[9])
	else:
		sector_r = int(args[5])
		sector_w = int(args[9])
		speed_r = sector_r - prev_scetor_r
		speed_w = sector_w - prev_sector_w
		prev_scetor_r = sector_r
		prev_sector_w = sector_w
		log_str = '{0} {1} {2}\n'.format(ts, speed_r, speed_w)
		with open('{0}/disk.txt'.format(home), 'a') as f:
			f.write(log_str)
			f.close()
	# network
	result = subprocess.Popen(network.split(), stdout=subprocess.PIPE).communicate()[0]
	lines = result.split('\n')
	net_line = ''
	for l in lines:
		if if_name in l:
			net_line = l
			break
	args = net_line.split()
	if not init:
		prev_rx = int(args[1])
		prev_tx = int(args[9])
	else:
		rx = int(args[1])
		tx = int(args[9])
		rx_rate = float(rx - prev_rx) / 512
		tx_rate = float(tx - prev_tx) / 512
		prev_rx = rx
		prev_tx = tx
		log_str = '{0} {1} {2}\n'.format(ts, rx_rate, tx_rate)
		with open('{0}/net.txt'.format(home), 'a') as f:
			f.write(log_str)
			f.close()
	init = True
	time.sleep(0.5)

