#!/usr/bin/env python

import sys
import os

usg = "Usage ./.login.py cluster_tpye(spark/hadoop) cluster_name"

if len(sys.argv) != 3:
    print usg
    sys.exit()

cluster_type = sys.argv[1]
name = sys.argv[2]

if cluster_type == 'spark':
    cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -r us-west-2 --zone=us-west-2a login %s" % name
    os.system(cmd)
elif cluster_type == 'hadoop':
    cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -u ubuntu -r us-west-2 --zone=us-west-2a login %s" % name
    os.system(cmd)
else:
    print usg
    sys.exit()
