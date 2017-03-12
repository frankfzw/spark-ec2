#!/usr/bin/env python

import sys
import os

usg = "Usage ./destroy.py cluster_name slaves_only(y/n)"

if len(sys.argv) != 3:
    print usg
    sys.exit()

name = sys.argv[1]
slaves = sys.argv[2]

if slaves == 'y' or slaves == 'Y':
    cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a delete-slaves %s" % name
    os.system(cmd)
elif slaves == 'n' or slaves == 'N':
    cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a destroy %s" % name
    os.system(cmd)
else:
    print usg
    sys.exit()
