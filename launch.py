#!/usr/bin/env python

import sys
import os

usg = "Usage ./.launch.py cluster_name slave_number existing_master(y/n)"

if len(sys.argv) != 4:
    print usg
    sys.exit()

name = sys.argv[1]
slaves_num = int(sys.argv[2])
master_flag = sys.argv[3]


# cmd = "./spark-ec2 -k scache -i ~/SCache/scache.pem -s %d -a ami-a3f67ac3 -u ubuntu -t t2.micro -r us-west-2 --zone=us-west-2a --hadoop-major-version=yarn --no-ganglia launch %s" % (slaves_num, name)
if master_flag == 'y' or master_flag == 'Y':
	cmd = './spark-ec2 -k scache -i ~/SCache/scache.pem -s %d -a ami-0f8c036f -u ubuntu -t m4.xlarge -r us-west-2 --zone=us-west-2a --hadoop-major-version=yarn --use-existing-master --no-ganglia launch %s' % (slaves_num, name)
	os.system(cmd)
elif master_flag == 'N' or master_flag == 'n':
	cmd = './spark-ec2 -k scache -i ~/SCache/scache.pem -s %d -a ami-0f8c036f -u ubuntu -t m4.xlarge -r us-west-2 --zone=us-west-2a --hadoop-major-version=yarn --no-ganglia launch %s' % (slaves_num, name)
	os.system(cmd)
else:
	print usg
	sys.exit()
