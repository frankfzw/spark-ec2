#!/usr/bin/env python

import sys
import os

usg = "Usage ./start-stop.py start/stop cluster_name"

if len(sys.argv) != 3:
    print usg
    sys.exit()

action = sys.argv[1]
name = sys.argv[2]

cmd = ''

if action == 'start':
    cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a -u ubuntu --hadoop-major-version=yarn --no-ganglia start %s" % name
    os.system(cmd)
elif action == 'stop':
    cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a -u ubuntu stop %s" % name
    os.system(cmd)
else:
    print usg

