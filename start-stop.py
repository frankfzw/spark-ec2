#!/usr/bin/env python

import sys
import os

usg = "Usage ./start-stop.py start/stop cluster_type(spark/hadoop) cluster_name"

if len(sys.argv) != 4:
    print usg
    sys.exit()

action = sys.argv[1]
cluster_type = sys.argv[2]
name = sys.argv[3]

cmd = ''

if cluster_type == 'spark':
    if action == 'start':
        cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a --hadoop-major-version=yarn --no-ganglia start %s" % name
        os.system(cmd)
    elif action == 'stop':
        cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a stop %s" % name
        os.system(cmd)
    else:
        print usg
elif cluster_type == 'hadoop':
    if action == 'start':
        cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a -u ubuntu --hadoop-major-version=yarn --no-ganglia start %s" % name
        os.system(cmd)
    elif action == 'stop':
        cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a -u ubuntu stop %s" % name
        os.system(cmd)
    else:
        print usg
else:
    print usg
