#!/usr/bin/env python

import sys
import os

usg = "Usage ./.launch.py cluster_name slave_number"

if len(sys.argv) != 3:
    print usg
    sys.exit()

name = sys.argv[1]
slaves_num = int(sys.argv[2])


cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -s %d -a ami-5e63d13e -u ubuntu -t m4.xlarge -r us-west-2 --zone=us-west-2a --hadoop-major-version=yarn --no-ganglia launch %s" % (slaves_num, name)
os.system(cmd)
