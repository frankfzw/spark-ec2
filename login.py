#!/usr/bin/env python

import sys
import os

usg = "Usage ./.login.py cluster_name"

if len(sys.argv) != 2:
    print usg
    sys.exit()

name = sys.argv[1]


cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -u ubuntu -r us-west-2 --zone=us-west-2a login %s" % name
os.system(cmd)
